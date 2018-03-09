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


def neighbors(loc):
    x, y = loc
    return [  # right
        (x+1, y),
        (x+1, y+1),
        # top
        (x, y+1),
        (x-1, y+1),
        # left
        (x-1, y),
        (x-1, y-1),
        # low
        (x, y-1),
        (x+1, y-1)]


def summed_spiral_gen():
    "an infinite generator"
    spiral = {}
    for loc in spiralgen():
        spiral[loc] = sum(spiral.get(x, 0) for x in neighbors(loc)) or 1
        yield spiral[loc]


def first(interable):
    "returns the first item in the interable"
    return next(iter(interable))


if __name__ == "__main__":
    PUZZLEINPUT = 361527
    RESULT = first(x for x in summed_spiral_gen() if x > PUZZLEINPUT)
    print(f"Input: {PUZZLEINPUT}, Result: {RESULT}")
