import sys
from utils.log import log

puzzle_input = [int(x) for x in sys.stdin.read().split('\n')]


def find_sum(puzzle_input, start, end, target):
    for i in range(start, end):
        for j in range(i + 1, end):
            if puzzle_input[i] + puzzle_input[j] == target:
                return True
    return False


@log
def a(puzzle_input):
    preamble_length = 25
    for offset in range(preamble_length, len(puzzle_input)):
        if not find_sum(puzzle_input, offset - preamble_length, offset, puzzle_input[offset]):
            return puzzle_input[offset]


def find_operands(puzzle_input, start, target):
    total = 0
    used = []
    for i in range(start, len(puzzle_input)):
        total += puzzle_input[i]
        if total > target:
            return []
        used.append(puzzle_input[i])
        if total == target:
            return used
    return []


@log
def b(puzzle_input, target):
    for offset in range(len(puzzle_input)):
        operands = find_operands(puzzle_input, offset, target)
        if len(operands) > 0:
            break
    return min(operands) + max(operands)


target = a(puzzle_input)
b(puzzle_input, target)
