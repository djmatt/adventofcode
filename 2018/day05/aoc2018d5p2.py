from operator import itemgetter


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
            return polymer


def aoc2018d5p2(polymer):
    polymer = aoc2018d5p1(polymer)

    all_results = []
    for letter in set(polymer.lower()):
        test = polymer.replace(letter, '')
        test = test.replace(letter.upper(), '')

        result = aoc2018d5p1(test)

        all_results.append((letter, len(result)))

    shortest = min(all_results, key=itemgetter(1))

    return shortest[1]


if __name__ == "__main__":

    TESTCASES = [('dabAcCaCBAcCcaDA', 4)]

    for case, expected in TESTCASES:
        result = aoc2018d5p2(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day05\\input.txt") as infile:
        PUZZLEINPUT = infile.readline().strip()
        RESULT = aoc2018d5p2(PUZZLEINPUT)
        print(f"Result is {RESULT}")
