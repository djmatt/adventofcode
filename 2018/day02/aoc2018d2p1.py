from collections import Counter


def count_dupes(letters):
    "get count of duplicate letters, we're only interested in counts of 2 and 3"
    uniques = set(letters)
    for unique in uniques:
        count = list(letters).count(unique)
        if 1 < count < 4:
            yield count


def get_count_of(num, num_sets):
    return sum(1 for nums in num_sets if num in nums)


def aoc2018d2p1(boxIDs):
    # count up the duplicates, collecting only 2 and 3 in sets
    IDs = [set(count_dupes(boxID)) for boxID in boxIDs]
    # filter out empty sets
    IDs = [ID for ID in IDs if bool(ID)]
    # sum up number of 2s and 3s
    twos, threes = get_count_of(2, IDs), get_count_of(3, IDs)
    return twos * threes


def aoc2018d2p1_alt(boxIDs):
    "from reddit"
    sum2 = sum(1 for c in (Counter(id) for id in boxIDs) if 2 in c.values())
    sum3 = sum(1 for c in (Counter(id) for id in boxIDs) if 3 in c.values())
    return sum2 * sum3


if __name__ == "__main__":
    TESTCASES = [(["abcdef",
                   "bababc",
                   "abbcde",
                   "abcccd",
                   "aabcdd",
                   "abcdee",
                   "ababab"], 12)]

    for case, expected in TESTCASES:
        result = aoc2018d2p1(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day02\\input.txt") as infile:
        PUZZLEINPUT = [line.strip() for line in infile.readlines()]
        RESULT = aoc2018d2p1(PUZZLEINPUT)
        print(f"Result is {RESULT}")
