

def jumper(instructions):
    status = instructions
    LO, HI = 0, len(status)
    step = index = 0
    while(LO <= index < HI):
        jump_n = status[index]
        status[index] += 1
        index += jump_n
        step += 1
    return step


if __name__ == "__main__":
    TESTCASES = [([0, 3, 0, 1, -3], 5)]

    for instructions, expected in TESTCASES:
        result = jumper(instructions)
        assert(result == expected)

    PUZZLEFILENAME = '.\\2017\\day05\\input.txt'
    with open(PUZZLEFILENAME) as infile:
        instructions = [int(x) for x in infile.readlines()]

    result = jumper(instructions)
    print(result)
