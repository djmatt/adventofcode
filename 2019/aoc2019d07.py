from aocd.models import Puzzle, User
from collections import deque
from collections.abc import Iterable
from itertools import permutations


class IntCodeComputer(object):

    def __init__(self, program):
        self.__origProg = program[:]
        self.__program = program[:]
        self.__pc = 0
        self.__inputs = deque()
        self.__outputs = []
        self.__operation = {
            1: self.__add,
            2: self.__mult,
            3: self.__getinput,
            4: self.__storeoutput,
            5: self.__jumptrue,
            6: self.__jumpfalse,
            7: self.__lessthan,
            8: self.__equals,
            99: self.__endprogram
        }
        self.__opcount = {
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

    def __add(self, operands):
        self.__program[operands[2]] = self.__program[operands[0]] + \
            self.__program[operands[1]]

    def __mult(self, operands):
        self.__program[operands[2]] = self.__program[operands[0]] * \
            self.__program[operands[1]]

    def __getinput(self, operands):
        self.__program[operands[0]] = self.__inputs.popleft()

    def __storeoutput(self, operands):
        self.__outputs.append(self.__program[operands[0]])

    def __jumptrue(self, operands):
        self.__pc = self.__program[operands[1]] - 3 \
            if self.__program[operands[0]] != 0 else self.__pc

    def __jumpfalse(self, operands):
        self.__pc = self.__program[operands[1]] - 3 \
            if self.__program[operands[0]] == 0 else self.__pc

    def __lessthan(self, operands):
        self.__program[operands[2]] = int(
            self.__program[operands[0]] < self.__program[operands[1]])

    def __equals(self, operands):
        self.__program[operands[2]] = int(
            self.__program[operands[0]] == self.__program[operands[1]])

    def __endprogram(self, operands):
        pass
        # print("That's all folks!")

    def __decode(self):
        instruction = self.__program[self.__pc]
        strcode = f"{instruction:05d}"
        opcode = int(strcode[3:])
        modes = tuple([bool(int(strcode[2])),
                       bool(int(strcode[1])),
                       bool(int(strcode[0]))])
        operands = tuple(self.__pc+i+1 if modes[i] else self.__program[self.__pc+i+1]
                         for i in range(self.__opcount[opcode]-1))

        # print for debug
        # print(f"PC: {self.__pc:03d}; Opcode: {opcode:02d};  Operands: {operands}")

        return opcode, operands

    def __proccesingloop(self):
        opcode = 0
        while opcode != 99:
            # decode current instruction for opcode and operands
            opcode, operands = self.__decode()
            # Carry out instruction
            self.__operation[opcode](operands)
            # Update PC
            self.__pc += self.__opcount[opcode]

    def run(self, inputs):
        self.__pc = 0
        self.__program = self.__origProg[:]
        if isinstance(inputs, Iterable):
            self.__inputs.extend(inputs)
        else:
            self.__inputs.append(inputs)
        self.__outputs = []
        self.__proccesingloop()

        return self.__outputs[:]


if __name__ == "__main__":
    # Get Puzzle data
    p = Puzzle(year=2019, day=7)
    program = [int(x) for x in p.input_data.split(',')]

    ICC = IntCodeComputer(program)

    # Part 1
    results = dict()
    for phases in permutations(range(0, 5)):
        signal = 0
        for phase in phases:
            signal = ICC.run([phase, signal]).pop()
        results[phases] = signal

    maxResult = max(results, key=results.get)
    print(f"Max Phases order {maxResult} generates {results[maxResult]} ")

    # Part 2
