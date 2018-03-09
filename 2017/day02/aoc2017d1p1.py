inputfile = ".\\2017\\day02\\input.txt"


def rowdiffs(filename):
    with open(filename) as infile:
        for line in infile:
            nums = [int(x) for x in line.split()]
            diff = max(nums) - min(nums)
            yield diff


checksum = sum(rowdiffs(inputfile))
print(f"Checksum {checksum}")
