import sys
from utils.log import log

puzzle_input = [int(x) for x in sys.stdin.read().split('\n')]


@log
def a(puzzle_input):
    for i, n in enumerate(puzzle_input):
        for _, m in enumerate(puzzle_input[i:]):
            if n + m == 2020:
                return n * m


@log
def b(puzzle_input):
    for i, n in enumerate(puzzle_input):
        for j, m in enumerate(puzzle_input[i:]):
            for _, o in enumerate(puzzle_input[j:]):
                if n + m + o == 2020:
                    return n * m * o


a(puzzle_input)
b(puzzle_input)
