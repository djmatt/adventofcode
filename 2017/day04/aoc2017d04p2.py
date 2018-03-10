
def test_pw(pw: str) -> bool:
    # seperate the pass phrase into phrases
    phrases = pw.split()
    # sort the letters in each phrase
    phrases = [''.join(sorted(phrase)) for phrase in phrases]
    # now remove duplicates
    others = list(set(phrases))
    return len(phrases) == len(others)


INTPUTFILE = ".\\2017\\day04\\input.txt"

if __name__ == "__main__":
    TESTCASES = [('abcde fghij', True),
                 ('abcde xyz ecdab', False),
                 ('a ab abc abd abf abj', True),
                 ('iiii oiii ooii oooi oooo', True),
                 ('oiii ioii iioi iiio', False)]

    for testcase, expected in TESTCASES:
        result = test_pw(testcase)
        assert result == expected

    with open(INTPUTFILE) as infile:
        result = sum(int(test_pw(pw)) for pw in infile)

    print(f"Number of valid passphrases: {result}")
