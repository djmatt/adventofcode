inputfile = ".\\2017\\day02\\input.txt"


def rowdiffs(filename):
    with open(filename) as infile:
        for line in infile:
            nums = [int(x) for x in line.split()]
            quotient = (x//y for x in nums for y in nums if x !=
                        y if x % y == 0)
            yield from quotient


checksum = sum(rowdiffs(inputfile))
print(f"Checksum {checksum}")
