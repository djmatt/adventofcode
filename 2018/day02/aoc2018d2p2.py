def aoc2018d2p2(boxIDs):
    for index in range(len(boxIDs[0])):
        # remove one letter from each of the IDs
        IDs = [ID[:index] + ID[index+1:] for ID in boxIDs]
        # are there any 2 that match?
        if len(IDs) != len(set(IDs)):
            # if so search for the match?
            for ID in IDs:
                if IDs.count(ID) > 1:
                    return ID


if __name__ == "__main__":
    TESTCASES = [(["abcde",
                   "fghij",
                   "klmno",
                   "pqrst",
                   "fguij",
                   "axcye",
                   "wvxyz"], "fgij")]

    for case, expected in TESTCASES:
        result = aoc2018d2p2(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day02\\input.txt") as infile:
        PUZZLEINPUT = [line.strip() for line in infile.readlines()]
        RESULT = aoc2018d2p2(PUZZLEINPUT)
        print(f"Result is {RESULT}")
