from aocd import submit
from aocd.models import Puzzle, User
from pathlib import Path
from itertools import product

pc = 0


def add(program, operands):
    program[operands[2]] = program[operands[0]] + program[operands[1]]


def mult(program, operands):
    program[operands[2]] = program[operands[0]] * program[operands[1]]


def getinput(program, operands):
    progInput = input("Provide me a number: ")
    program[operands[0]] = int(progInput)


def printoutput(program, operands):
    print(f"Diagnostic Code: {program[operands[0]]}")


def jumptrue(program, operands):
    global pc
    pc = program[operands[1]]-3 if program[operands[0]] != 0 else pc


def jumpfalse(program, operands):
    global pc
    pc = program[operands[1]]-3 if program[operands[0]] == 0 else pc


def lessthan(program, operands):
    program[operands[2]] = int(program[operands[0]] < program[operands[1]])


def equals(program, operands):
    program[operands[2]] = int(program[operands[0]] == program[operands[1]])


def endprogram(program, operands):
    print("That's all folks!")


def decode(program):
    global pc
    instruction = program[pc]
    strcode = f"{instruction:05d}"
    opcode = int(strcode[3:])
    modes = tuple([bool(int(strcode[2])),
                   bool(int(strcode[1])),
                   bool(int(strcode[0]))])
    operands = tuple(pc+i+1 if modes[i] else program[pc+i+1]
                     for i in range(opcount[opcode]-1))

    # print for debug
    print(f"PC: {pc:03d}; Opcode: {opcode:02d};  Operands: {operands}")

    return opcode, operands


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


def proccesingloop(program):
    global pc
    opcode = 0
    while opcode != 99:
        # decode current instruction for opcode and operands
        opcode, operands = decode(program)
        # Carry out instruction
        operation[opcode](program, operands)
        # Update PC
        pc += opcount[opcode]


if __name__ == "__main__":
    # Get Puzzle data
    p = Puzzle(year=2019, day=5)
    input_data = [int(x) for x in p.input_data.split(',')]
    program = input_data[:]

    proccesingloop(program)
