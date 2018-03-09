from itertools import islice


def spiralgen():
    '''
    Infinite spiral generator
    '''
    loc = (0, 0)
    yield loc
    ring = 1
    while True:
        # move right for the next ring
        loc = (loc[0]+1, loc[1])
        yield loc
        # move up right side
        for _ in range((ring * 2)-1):
            loc = (loc[0], loc[1]+1)
            yield loc
        # move left along the top
        for _ in range(ring * 2):
            loc = (loc[0]-1, loc[1])
            yield loc
        # move down left side
        for _ in range(ring * 2):
            loc = (loc[0], loc[1]-1)
            yield loc
        # move right along bottom
        for _ in range(ring * 2):
            loc = (loc[0]+1, loc[1])
            yield loc
        ring += 1


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    # taken from the itertools example recipes
    return next(islice(iterable, n, None), default)


def manhanttan_length(loc):
    "Returns the manhanttan length from (0, 0) to loc"
    return sum(abs(x) for x in loc)


if __name__ == "__main__":
    TESTCASES = [(1, 0),
                 (12, 3),
                 (23, 2),
                 (1024, 31)]

    for input, expected in TESTCASES:
        result = manhanttan_length(nth(spiralgen(), input-1))
        print(f"Input: {input},  Result: {result},  Expected: {expected}")
        assert result == expected

    PUZZLEINPUT = 361527
    RESULT = manhanttan_length(nth(spiralgen(), PUZZLEINPUT - 1))
    print(f"Puzzle Input: {PUZZLEINPUT},  Result: {RESULT}")
