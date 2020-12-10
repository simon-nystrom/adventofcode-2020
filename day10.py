import sys
from utils.log import log

puzzle_input = sorted([int(x) for x in sys.stdin.read().split('\n')])
puzzle_input = [0] + puzzle_input + [puzzle_input[len(puzzle_input) - 1] + 3]

@log
def a(puzzle_input):
    prev_joltage = 0
    num_1_diff, num_3_diff = 0, 1
    for joltage in puzzle_input:
        diff = joltage - prev_joltage
        if diff == 1:
            num_1_diff += 1
        if diff == 3:
            num_3_diff += 1
        prev_joltage = joltage
    return num_1_diff * num_3_diff

def count(puzzle_input, start = 1, num = 0):
    total = 0
    for i in range(start, len(puzzle_input) - 1):
        can_remove = puzzle_input[i + 1] - puzzle_input[i - 1] <= 3
        if can_remove:
            copy = puzzle_input.copy()
            del copy[i]
            total += count(copy, i, num + 1)
    total += 1
    return total

@log
def b(puzzle_input):
    # Ugliest divide and conquer to ever see the light
    return count(puzzle_input[0:40]) * count(puzzle_input[40:60]) * count(puzzle_input[60:97])

a(puzzle_input)
b(puzzle_input)
