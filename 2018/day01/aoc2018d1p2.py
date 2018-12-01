from itertools import cycle, accumulate


def gen_freqs(nums):
    current = 0
    for num in nums:
        yield current
        current = current + num


def aoc2018d1p2(nums):
    chained = cycle(nums)
    seen = set()
    for freq in gen_freqs(chained):
        if(freq in seen):
            return freq
        else:
            seen.add(freq)


def first(interable):
    "returns the first item in the interable"
    return next(iter(interable))


def aoc2018d1p2_alternate(nums):
    "as seen on reddit"
    seen = set()
    return first(freq for freq in accumulate(cycle(nums)) if freq in seen or seen.add(freq))


if __name__ == "__main__":
    TESTCASES = [([+1, -2, +3, +1], 2),
                 ([+1, -1], 0),
                 ([+3, +3, +4, -2, -4], 10),
                 ([-6, +3, +8, +5, -6], 5),
                 ([+7, +7, -2, -7, -4], 14)]

    for case, expected in TESTCASES:
        result = aoc2018d1p2(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day01\\input.txt") as infile:
        PUZZLEINPUT = [int(num) for num in infile.readlines()]
        RESULT = aoc2018d1p2(PUZZLEINPUT)
        print(f"Result is {RESULT}")

        RESULT = aoc2018d1p2_alternate(PUZZLEINPUT)
        print(f"Result is {RESULT}")
