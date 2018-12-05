from parse import parse
from itertools import product, combinations
from datetime import datetime
from operator import itemgetter


def aoc2018d4p1(inputs):
    def readInputs(inputs):
        "converts input into (datetime, message) tuple"
        for i in inputs:
            p = parse('[{}] {}', i)
            time, message = p
            time = datetime.strptime(time, '%Y-%m-%d %H:%M')
            print(time, message)
            yield (time, message)

    # read the inputs,
    msgs = [i for i in readInputs(inputs)]
    # sort by time
    msgs.sort(key=itemgetter(0))

    # tally up the minutes asleep
    guards = {}
    guard = awake = asleep = 0
    for time, msg in msgs:
        print(time, msg)
        if 'shift' in msg:
            p = parse('{} #{:d} {}', msg)
            guard = p[1]
        elif 'asleep' in msg:
            asleep = int(time.minute)
        elif 'wakes' in msg:
            awake = int(time.minute)
            if guard not in guards:
                guards[guard] = [0]*60
            for minute in range(asleep, awake):
                guards[guard][minute] += 1

    for guard, time in guards.items():
        print(guard, time)

    # get the laziest guard
    laziest = max(guards, key=lambda g: sum(guards[g]))
    print(laziest)

    # get the most likely time asleep
    best_time = guards[laziest].index(max(guards[laziest]))
    print(best_time)

    return best_time * laziest


if __name__ == "__main__":

    TESTCASES = [(('[1518-11-01 00:00] Guard #10 begins shift',
                   '[1518-11-01 00:30] falls asleep',
                   '[1518-11-02 00:40] falls asleep',
                   '[1518-11-01 23:58] Guard #99 begins shift',
                   '[1518-11-05 00:03] Guard #99 begins shift',
                   '[1518-11-02 00:50] wakes up',
                   '[1518-11-03 00:29] wakes up',
                   '[1518-11-03 00:05] Guard #10 begins shift',
                   '[1518-11-01 00:05] falls asleep',
                   '[1518-11-04 00:02] Guard #99 begins shift',
                   '[1518-11-01 00:25] wakes up',
                   '[1518-11-05 00:45] falls asleep',
                   '[1518-11-04 00:46] wakes up',
                   '[1518-11-04 00:36] falls asleep',
                   '[1518-11-03 00:24] falls asleep',
                   '[1518-11-01 00:55] wakes up',
                   '[1518-11-05 00:55] wakes up'), 240)]

    for case, expected in TESTCASES:
        result = aoc2018d4p1(case)
        print(f"Input: {case},  Result: {result},  Expected: {expected}")
        assert result == expected

    with open(".\\2018\\day04\\input.txt") as infile:
        PUZZLEINPUT = [line.strip() for line in infile.readlines()]
        RESULT = aoc2018d4p1(PUZZLEINPUT)
        print(f"Result is {RESULT}")
