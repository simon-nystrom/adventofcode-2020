import sys
from utils.log import log

puzzle_input = [x for x in sys.stdin.read().split('\n')]


def check_slope(r, d):
    num_trees = 0
    offset = 0
    for i in range(0, len(puzzle_input), d):
        if puzzle_input[i][offset % len(puzzle_input[i])] == '#':
            num_trees += 1
        offset += r
    return num_trees


@log
def a(puzzle_input):
    return check_slope(3, 1)


@log
def b(puzzle_input):
    result = 1
    result *= check_slope(1, 1)
    result *= check_slope(3, 1)
    result *= check_slope(5, 1)
    result *= check_slope(7, 1)
    result *= check_slope(1, 2)
    return result


a(puzzle_input)
b(puzzle_input)
