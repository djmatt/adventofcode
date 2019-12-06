from aocd import submit
from aocd.models import Puzzle, User
from pathlib import Path
from itertools import product


# Shamlessly stolen from https://github.com/norvig/pytudes/blob/master/ipynb/Advent%202017.ipynb
def X(point): return point[0]


def Y(point): return point[1]


origin = (0, 0)
HEADINGS = UP, LEFT, DOWN, RIGHT = (0, 1), (-1, 0), (0, -1), (1, 0)


def turn_right(heading): return HEADINGS[HEADINGS.index(heading) - 1]


def turn_around(heading): return HEADINGS[HEADINGS.index(heading) - 2]


def turn_left(heading): return HEADINGS[HEADINGS.index(heading) - 3]


def mapt(fn, *args):
    "Do a map, and make the results into a tuple."
    return tuple(map(fn, *args))


def add(A, B):
    "Element-wise addition of two n-dimensional vectors."
    return mapt(sum, zip(A, B))


def neighbors4(point):
    "The four neighboring squares."
    x, y = point
    return ((x, y-1),
            (x-1, y),           (x+1, y),
            (x, y+1))


def neighbors8(point):
    "The eight neighboring squares."
    x, y = point
    return ((x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y),             (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1))


def cityblock_distance(P, Q=origin):
    "Manhatten distance between two points."
    return sum(abs(p - q) for p, q in zip(P, Q))

############


dir2heading = {'L': LEFT, 'l': LEFT,
               'R': RIGHT, 'r': RIGHT,
               'U': UP, 'u': UP,
               'D': DOWN, 'd': DOWN}


def genPath(directions):
    here = origin
    for move in directions:
        heading, dist = dir2heading[move[0]], int(move[1:])
        for _ in range(dist):
            here = add(here, heading)
            yield here


def part1(puzzle_data):
    wire1, wire2 = puzzle_data.splitlines()
    directions = wire1.split(',')
    path1 = list(genPath(directions))
    directions = wire2.split(',')
    path2 = list(genPath(directions))

    intersections = set(path1) & set(path2)

    closest = min(intersections, key=cityblock_distance)

    return cityblock_distance(closest)


def part2(puzzle_data):
    wire1, wire2 = puzzle_data.splitlines()
    directions = wire1.split(',')
    path1 = list(genPath(directions))
    directions = wire2.split(',')
    path2 = list(genPath(directions))

    intersections = set(path1) & set(path2)

    pathsums = [path1.index(intersection) + path2.index(intersection) + 2
                for intersection in intersections]

    return min(pathsums)


if __name__ == "__main__":
    # Get Puzzle data
    p = Puzzle(year=2019, day=3)

    # Part one
    # p.answer_a = part1(input_data)
    print(part1(p.input_data[:]))

    # Part two
    # p.answer_b = part2(input_data)
    print(part2(p.input_data[:]))
    # print(part2('R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'))
    # print(part2('R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'))
