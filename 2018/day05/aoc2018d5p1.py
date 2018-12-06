def aoc2018d5p1(polymer):
    def react(polymer):
        if len(polymer) < 2:
            return polymer
        else:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                polymer = polymer.replace(c + c.upper(), '')
                polymer = polymer.replace(c.upper() + c, '')
            return polymer

    while True:
        before = len(polymer)
        polymer = react(polymer)
        after = len(polymer)
        if before == after:
            return len(polymer)


if __name__ == "__main__":

    TESTCASES = [('a', 1),
                 ('aA', 0),
                 ('abBA', 0),
                 ('aabAAB', 6),
                 ('dabAcCaCBAcCcaDA', 10)]

    for case, expected in TESTCASES:
        result = aoc2018d5p1(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day05\\input.txt") as infile:
        PUZZLEINPUT = infile.readline().strip()
        RESULT = aoc2018d5p1(PUZZLEINPUT)
        print(f"Result is {RESULT}")
