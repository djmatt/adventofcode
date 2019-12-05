from aocd import submit
from aocd.models import Puzzle, User
from pathlib import Path


def part1(modules):
    return sum(module//3 - 2 for module in modules)


def part2(modules):
    def genFuels(module):
        fuel = module//3 - 2
        while fuel >= 0:
            yield fuel
            fuel = fuel // 3 - 2

    def moduleFuel(module):
        return sum(genFuels(module))

    return(sum(moduleFuel(module) for module in modules))


if __name__ == "__main__":

    with open(Path.cwd()/"session.id") as id_file:
        user = User(id_file.readline())

    # Get Puzzle data
    p = Puzzle(year=2019, day=1, user=user)
    input_data = [int(x) for x in p.input_data.splitlines()]

    # Part one
    # p.answer_a = part1(input_data)
    print(part1(input_data))

    # Part two
    # p.answer_b = part2(input_data)
    print(part2(input_data))
