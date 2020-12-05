import sys
from math import ceil
from utils.log import log

puzzle_input = [x for x in sys.stdin.read().split('\n')]


def bisect(start, end, segment):
    if segment == 'F' or segment == 'L':
        return (start, (end - start) // 2 + start)
    else:
        return (ceil((end - start) / 2) + start, end)


def get_seat_id(seat_spec):
    low_row, high_row = 0, 127
    for i in range(7):
        (low_row, high_row) = bisect(low_row, high_row, seat_spec[i])
    low_col, high_col = 0, 7
    for i in range(3):
        (low_col, high_col) = bisect(low_col, high_col, seat_spec[7 + i])
    return low_row * 8 + low_col


@log
def a(puzzle_input):
    highest_seat_id = 0
    for seat_spec in puzzle_input:
        highest_seat_id = max(get_seat_id(seat_spec), highest_seat_id)
    return highest_seat_id


@log
def b(puzzle_input):
    seat_ids = []
    for seat_spec in puzzle_input:
        seat_ids.append(get_seat_id(seat_spec))

    seat_ids = sorted(seat_ids)
    for i in range(8, len(seat_ids) - 8):
        if seat_ids[i] != seat_ids[i + 1] - 1:
            return seat_ids[i] + 1


a(puzzle_input)
b(puzzle_input)
