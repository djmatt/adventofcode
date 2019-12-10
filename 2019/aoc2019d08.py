from aocd.models import Puzzle
from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def first(interable):
    "returns the first item in the interable"
    return next(iter(interable))


def countZeros(layer: str):
    return layer.count('0')


def part1(puzzle_input):
    layers = grouper(puzzle_input, 25*6)
    layer = min(layers, key=countZeros)
    return layer.count('1') * layer.count('2')


def part2(puzzle_input):
    layers = grouper(puzzle_input, 25*6)
    pixels = zip(*layers)
    pixels = [first(layer for layer in pixel if layer != '2')
              for pixel in pixels]
    lines = grouper(pixels, 25)
    for line in lines:
        line = ''.join(line)
        print(line.replace('0', ' '))

    return None


if __name__ == "__main__":
    # Get Puzzle data
    p = Puzzle(year=2019, day=8)
    input_data = p.input_data

    print(part1(input_data))

    part2(input_data)
