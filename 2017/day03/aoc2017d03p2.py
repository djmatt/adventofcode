from collections import deque
from itertools import islice, takewhile

def spiralgen():
    '''
    Infinite spiral generator
    '''
    loc = (0, 0)
    yield loc
    ring = 1
    while True:
        #move right for the next ring
        loc = (loc[0]+1, loc[1])
        yield loc
        #move up right side
        for _ in range( (ring * 2)-1):
            loc = (loc[0], loc[1]+1)
            yield loc
        #move left along the top
        for _ in range(ring * 2):
            loc = (loc[0]-1, loc[1])
            yield loc
        #move down left side
        for _ in range(ring * 2):
            loc = (loc[0], loc[1]-1)
            yield loc
        #move right along bottom
        for _ in range(ring * 2):
            loc = (loc[0]+1, loc[1])
            yield loc
        ring += 1

TESTCASES = [(1,0),
            (12,3),
            (23,2),
            (1024,31)]

for input, expected in TESTCASES:
    spiral = deque(islice(spiralgen(), input))
    result = sum([abs(x) for x in spiral.pop()])
    print(f"Input: {input},  Result: {result},  Expected: {expected}")

PUZZLEINPUT = 361527

def neighbors(loc):
    x,y = loc
    return [#right
            (x+1,y),
            (x+1,y+1),
            #top
            (x,y+1),
            (x-1,y+1),
            #left
            (x-1,y),
            (x-1,y-1),
            #low
            (x,y-1),
            (x+1,y-1)]


spiral = {}
for loc in spiralgen():
    if spiral:
        spiral[loc] = sum(spiral.get(x,0) for x in neighbors(loc))
    else:
        spiral[loc] = 1

    print(f"Result: {spiral[loc]}")

    if spiral[loc] > PUZZLEINPUT:
        break
