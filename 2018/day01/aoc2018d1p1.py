def aoc2018d1p1(nums):
    return sum(nums)


if __name__ == "__main__":
    TESTCASES = [([+1, -2, +3, +1], 3),
                 ([+1, +1, +1], 3),
                 ([+1, +1, -2], 0),
                 ([-1, -2, -3], -6)]

    for case, expected in TESTCASES:
        result = aoc2018d1p1(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day01\\input.txt") as infile:
        PUZZLEINPUT = [int(num) for num in infile.readlines()]
        RESULT = aoc2018d1p1(PUZZLEINPUT)
        print(f"Result is {RESULT}")
