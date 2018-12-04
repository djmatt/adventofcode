from parse import parse
from itertools import product, combinations


def aoc2018d3p1(inputs):
    def build_panel_set(num, x, y, w, h):
        return set(product(range(x, x+w), range(y, y+h)))

    panels = (build_panel_set(*input) for input in inputs)
    overlap = set.union(*(s & t for s, t in combinations(panels, 2)))
    return len(overlap)


if __name__ == "__main__":

    TESTCASES = [(([1, 1, 3, 4, 4],
                   [2, 3, 1, 4, 4],
                   [3, 5, 5, 2, 2]), 4)]

    for case, expected in TESTCASES:
        result = aoc2018d3p1(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day03\\input.txt") as infile:
        PUZZLEINPUT = set()
        for line in infile:
            p = parse('#{:d} @ {:d},{:d}: {:d}x{:d}', line)
            PUZZLEINPUT.add(tuple(p))

        RESULT = aoc2018d3p1(PUZZLEINPUT)
        print(f"Result is {RESULT}")
