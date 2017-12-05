inputfile = ".\\2017\\day2\\input.txt"

def rowdiffs(filename):
    with open(filename) as infile:
        for line in infile:
            nums = [int(x) for x in line.split()]
            diff = max(nums) - min(nums)
            yield diff

print(f"Checksum {sum(rowdiffs(inputfile))}")
