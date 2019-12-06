from aocd import submit
from aocd.models import Puzzle, User
from pathlib import Path
from itertools import product

pc = 0


def add(program, modes, operands):
    global pc
    param1 = program[pc+1] if modes[0] else program[operands[0]]
    param2 = program[pc+2] if modes[1] else program[operands[1]]
    param3 = pc+3 if modes[2] else operands[2]
    program[param3] = param1 + param2


def mult(program, modes, operands):
    global pc
    param1 = program[pc+1] if modes[0] else program[operands[0]]
    param2 = program[pc+2] if modes[1] else program[operands[1]]
    param3 = pc+3 if modes[2] else operands[2]
    program[param3] = param1 * param2


def getinput(program, modes, operands):
    global pc
    param1 = pc+1 if modes[0] else operands[0]
    progInput = input("Provide me a number: ")
    program[param1] = int(progInput)


def printoutput(program, modes, operands):
    global pc
    param1 = program[pc+1] if modes[0] else program[operands[0]]
    print(f"Diagnostic Code: {param1}")


def jumptrue(program, modes, operands):
    global pc
    param1 = program[pc+1] if modes[0] else program[operands[0]]
    param2 = program[pc+2] if modes[1] else program[operands[1]]
    pc = param2 if param1 != 0 else pc+3


def jumpfalse(program, modes, operands):
    global pc
    param1 = program[pc+1] if modes[0] else program[operands[0]]
    param2 = program[pc+2] if modes[1] else program[operands[1]]
    pc = param2 if param1 == 0 else pc+3


def lessthan(program, modes, operands):
    global pc
    param1 = program[pc+1] if modes[0] else program[operands[0]]
    param2 = program[pc+2] if modes[1] else program[operands[1]]
    param3 = pc+3 if modes[2] else operands[2]
    program[param3] = int(param1 < param2)


def equals(program, modes, operands):
    global pc
    param1 = program[pc+1] if modes[0] else program[operands[0]]
    param2 = program[pc+2] if modes[1] else program[operands[1]]
    param3 = pc+3 if modes[2] else operands[2]
    program[param3] = int(param1 == param2)


def endprogram(program, modes, operands):
    global pc
    print("That's all folks!")


def decode(instruction):
    global pc
    strcode = f"{instruction:05d}"
    opcode = int(strcode[3:])
    modes = tuple([bool(int(strcode[2])),
                   bool(int(strcode[1])),
                   bool(int(strcode[0]))])
    operands = tuple(program[pc+i+1] for i in range(opcount[opcode]-1))

    # print for debug
    modestr = ''.join(['P' if mode else 'I' for mode in modes])
    print(
        f"PC: {pc:03d}; Opcode: {opcode:02d}; Modes: {modestr}; Operands: {operands}")

    return opcode, modes, operands


operation = {
    1: add,
    2: mult,
    3: getinput,
    4: printoutput,
    5: jumptrue,
    6: jumpfalse,
    7: lessthan,
    8: equals,
    99: endprogram
}

opcount = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 3,
    6: 3,
    7: 4,
    8: 4,
    99: 1
}

incrementpc = {
    1: 4,
    2: 4,
    3: 2,
    4: 2,
    5: 0,
    6: 0,
    7: 4,
    8: 4,
    99: 1
}


def proccesingloop(program):
    global pc
    opcode = 0
    while opcode != 99:
        # get instruction from current pc
        instruction = program[pc]
        # decode instruction for opcode and modes
        opcode, modes, operands = decode(instruction)
        # Carry out instruction
        operation[opcode](program, modes, operands)
        # Update PC
        pc += incrementpc[opcode]


if __name__ == "__main__":

    # with open(Path.cwd()/"session.id") as id_file:
        # user = User(id_file.readline())

    # Get Puzzle data
    p = Puzzle(year=2019, day=5)
    input_data = [int(x) for x in p.input_data.split(',')]

    program = input_data[:]

    proccesingloop(program)
