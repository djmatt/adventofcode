from aocd import submit
from aocd.models import Puzzle, User
from pathlib import Path


def genMonotonic(n, prefix='', llimit=0):
    if n == 1:
        for d in range(llimit, 10):
            yield f'{prefix}{d}'
    else:
        for d in range(llimit, 10):
            cur = f'{prefix}{d}'
            yield from genMonotonic(n=n-1, prefix=cur, llimit=d)


def doubleADigit(numstrs):
    for numstr in numstrs:
        for i, num in enumerate(numstr):
            newstr = numstr[:]
            newstr = ''.join((newstr[:i], num*2, newstr[i+1:]))
            yield newstr


def doubleADigit2(numstrs):
    for numstr in numstrs:
        for i, num in enumerate(numstr):
            if numstr.count(num) == 1:
                newstr = numstr[:]
                newstr = ''.join((newstr[:i], num*2, newstr[i+1:]))
                yield newstr


def part1():
    lo, hi = 171309, 643603

    # gen monotonic numbers
    monotonic5 = genMonotonic(5)

    # gen doubled digit variations
    doubledDigitnumstr = doubleADigit(monotonic5)

    # convert to int
    doubledDigit = (int(num) for num in doubledDigitnumstr)

    # filter numbers between lo and hi
    filterednums = (num for num in doubledDigit if lo <= num <= hi)

    finalset = set(filterednums)

    return len(finalset)


def part2():
    lo, hi = 171309, 643603

    # gen monotonic numbers
    monotonic5 = genMonotonic(5)

    # gen doubled digit variations
    doubledDigitnumstr = doubleADigit2(monotonic5)

    # convert to int
    doubledDigit = (int(num) for num in doubledDigitnumstr)

    # filter numbers between lo and hi
    filterednums = (num for num in doubledDigit if lo <= num <= hi)

    finalset = set(filterednums)

    return len(finalset)


if __name__ == "__main__":
    # Part one
    print(part1())

    # Part two
    print(part2())
    lo, hi = 171309, 643603
    finalset = sorted(list(set(num for num in (int(numstr)
                                               for numstr in doubleADigit2(genMonotonic(5)))
                               if lo <= num <= hi)))

    # print(finalset)
