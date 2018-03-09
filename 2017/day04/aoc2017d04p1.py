
def test_pw(pw: str) -> bool:
    # seperate the pass phrase into phrases
    phrases = pw.split()
    # now remove duplicates
    others = list(set(phrases))
    return len(phrases) == len(others)


INTPUTFILE = ".\\2017\\day04\\input.txt"

if __name__ == "__main__":
    TESTCASES = [('aa bb cc dd ee', True),
                 ('aa bb cc dd aa', False),
                 ('aa bb cc dd aaa', True)]

    for input, expected in TESTCASES:
        result = test_pw(input)
        assert result == expected

    with open(INTPUTFILE) as infile:
        result = sum(int(test_pw(pw)) for pw in infile)

    print(f"Number of valid passphrases: {result}")
