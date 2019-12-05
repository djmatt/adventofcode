from aocd import submit
from aocd.models import Puzzle, User
from pathlib import Path
from itertools import product

instructions = {
    1: lambda a, b: a+b,
    2: lambda a, b: a*b
}


def part1(program):
    index = 0
    opcode = program[index]
    while opcode == 1 or opcode == 2:
        inputs = program[index+1:index+3]
        destination = program[index+3]
        # print(f"Instruction: {opcode},{inputs[0]},{inputs[1]},{destination}")
        operands = [program[p] for p in inputs]
        program[destination] = instructions[opcode](*operands)
        # print(f"Program: {program}")
        index += 4
        opcode = program[index]

    return program[0]


def part2(puzzle_data):
    for noun, verb in product(range(100), range(100)):
        program = puzzle_data[:]
        print(f"*-*{noun},{verb}*-*")
        program[1] = noun
        program[2] = verb
        if part1(program) == 19690720:
            break

    return 100 * noun + verb


if __name__ == "__main__":

    with open(Path.cwd()/"session.id") as id_file:
        user = User(id_file.readline())

    # Get Puzzle data
    p = Puzzle(year=2019, day=2, user=user)
    input_data = [int(x) for x in p.input_data.split(',')]

    # Part one
    part1program = input_data[:]
    part1program[1] = 12
    part1program[2] = 2
    # p.answer_a = part1(input_data)
    print(part1(part1program))

    # Part two
    part2program = input_data[:]
    # p.answer_b = part2(input_data)
    print(part2(part2program))
