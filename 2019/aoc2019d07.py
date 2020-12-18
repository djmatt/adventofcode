from aocd.models import Puzzle, User
from collections import deque
from collections.abc import Iterable
from itertools import permutations


class IntCodeComputer(object):

    def __init__(self, program):
        self._disk = program[:]
        self._ram = program[:]
        self._pc = 0
        self._inputs = deque()
        self._outputs = []
        self._operation = {
            1: self._add,
            2: self._mult,
            3: self._getinput,
            4: self._storeoutput,
            5: self._jumptrue,
            6: self._jumpfalse,
            7: self._lessthan,
            8: self._equals,
            99: self._endprogram
        }
        self._opcount = {
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

    def _add(self, operands):
        self._ram[operands[2]] = self._ram[operands[0]] + \
            self._ram[operands[1]]

    def _mult(self, operands):
        self._ram[operands[2]] = self._ram[operands[0]] * \
            self._ram[operands[1]]

    def _getinput(self, operands):
        self._ram[operands[0]] = self._inputs.popleft()

    def _storeoutput(self, operands):
        self._outputs.append(self._ram[operands[0]])

    def _jumptrue(self, operands):
        self._pc = self._ram[operands[1]] - 3 \
            if self._ram[operands[0]] != 0 else self._pc

    def _jumpfalse(self, operands):
        self._pc = self._ram[operands[1]] - 3 \
            if self._ram[operands[0]] == 0 else self._pc

    def _lessthan(self, operands):
        self._ram[operands[2]] = int(
            self._ram[operands[0]] < self._ram[operands[1]])

    def _equals(self, operands):
        self._ram[operands[2]] = int(
            self._ram[operands[0]] == self._ram[operands[1]])

    def _endprogram(self, operands):
        pass
        # print("That's all folks!")

    def _decode(self):
        instruction = self._ram[self._pc]
        strcode = f"{instruction:05d}"
        opcode = int(strcode[3:])
        modes = tuple([bool(int(strcode[2])),
                       bool(int(strcode[1])),
                       bool(int(strcode[0]))])
        operands = tuple(self._pc+i+1 if modes[i] else self._ram[self._pc+i+1]
                         for i in range(self._opcount[opcode]-1))

        # print for debug
        # print(f"PC: {self.__pc:03d}; Opcode: {opcode:02d};  Operands: {operands}")

        return opcode, operands

    def _proccesingloop(self):
        opcode = 0
        while opcode != 99:
            # decode current instruction for opcode and operands
            opcode, operands = self._decode()
            # Carry out instruction
            self._operation[opcode](operands)
            # Update PC
            self._pc += self._opcount[opcode]

    def run(self, inputs):
        self._pc = 0
        self._ram = self._disk[:]
        if isinstance(inputs, Iterable):
            self._inputs.extend(inputs)
        else:
            self._inputs.append(inputs)
        self._outputs = []
        self._proccesingloop()

        return self._outputs[:]


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
