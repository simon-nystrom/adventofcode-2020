import sys
from copy import deepcopy
from utils.log import log

puzzle_input = [list(x) for x in sys.stdin.read().split('\n')]

EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'

def is_down_right_occupied(p, x, y):
    return x + 1 < len(p[0]) and y + 1 < len(p) and p[y + 1][x + 1] == OCCUPIED

def is_down_left_occupied(p, x, y):
    return x - 1 >= 0 and y + 1 < len(p) and p[y + 1][x - 1] == OCCUPIED

def is_up_occupied(p, x, y):
    return y - 1 >= 0 and p[y - 1][x] == OCCUPIED

def is_down_occupied(p, x, y):
    return y + 1 < len(p) and p[y + 1][x] == OCCUPIED

def is_left_occupied(p, x, y):
    return x - 1 >= 0 and p[y][x - 1] == OCCUPIED

def is_right_occupied(p, x, y):
    return x + 1 < len(p[0]) and p[y][x + 1] == OCCUPIED

def is_up_left_occupied(p, x, y):
    return x - 1 >= 0 and y - 1 >= 0 and p[y - 1][x - 1] == OCCUPIED

def is_up_right_occupied(p, x, y):
    return x + 1 < len(p[0]) and y - 1 >= 0 and p[y - 1][x + 1] == OCCUPIED

def num_occupied_adjacent(p, x, y):
    num_occupied = 0
    if is_left_occupied(p, x, y):
        num_occupied += 1
    if is_right_occupied(p, x, y):
        num_occupied += 1
    if is_up_left_occupied(p, x, y):
        num_occupied += 1
    if is_down_right_occupied(p, x, y):
        num_occupied += 1
    if is_down_occupied(p, x, y):
        num_occupied += 1
    if is_up_occupied(p, x, y):
        num_occupied += 1
    if is_up_right_occupied(p, x, y):
        num_occupied += 1
    if is_down_left_occupied(p, x, y):
        num_occupied += 1
    return num_occupied
    
def count_occupied(grid):
    occupied_seats = 0
    for row in grid:
        for seat in row:
            if seat == OCCUPIED:
                occupied_seats += 1
    return occupied_seats

@log
def a(puzzle_input):
    unchanged = 0
    grid = deepcopy(puzzle_input)
    while unchanged != len(puzzle_input[0]) * len(puzzle_input):
        grid = deepcopy(puzzle_input)
        unchanged = 0
        for y in range(len(puzzle_input)):
            for x in range(len(puzzle_input[y])):
                if puzzle_input[y][x] == FLOOR:
                    unchanged += 1
                    continue
                num_occ = num_occupied_adjacent(puzzle_input, x, y)
                if puzzle_input[y][x] == EMPTY and num_occ == 0:
                    grid[y][x] = OCCUPIED
                elif puzzle_input[y][x] == OCCUPIED and num_occ >= 4:
                    grid[y][x] = EMPTY
                else:
                    unchanged += 1
        puzzle_input = deepcopy(grid)
    return count_occupied(grid)


def can_see_occupied_seat(p, x, y, delta_x, delta_y):
    i,j = x,y
    while i + delta_x >= 0 and i + delta_x < len(p[0]) and j + delta_y >= 0 and j + delta_y < len(p):
        i += delta_x
        j += delta_y
        if p[j][i] == FLOOR:
            continue
        return p[j][i] == OCCUPIED

def num_occupied_seen(p, x, y):
    num_occupied = 0
    if can_see_occupied_seat(p, x, y, -1, 0):
        num_occupied += 1
    if can_see_occupied_seat(p, x, y, 1, 0):
        num_occupied += 1
    if can_see_occupied_seat(p, x, y, -1, -1):
        num_occupied += 1
    if can_see_occupied_seat(p, x, y, 1, 1):
        num_occupied += 1
    if can_see_occupied_seat(p, x, y, 0, 1):
        num_occupied += 1
    if can_see_occupied_seat(p, x, y, 0, -1):
        num_occupied += 1
    if can_see_occupied_seat(p, x, y, 1, -1):
        num_occupied += 1
    if can_see_occupied_seat(p, x, y, -1, 1):
        num_occupied += 1
    return num_occupied

@log
def b(puzzle_input):
    unchanged = 0
    grid = deepcopy(puzzle_input)
    i = 0
    while unchanged != len(puzzle_input[0]) * len(puzzle_input):
        i += 1
        grid = deepcopy(puzzle_input)
        unchanged = 0
        for y in range(len(puzzle_input)):
            for x in range(len(puzzle_input[y])):
                if puzzle_input[y][x] == FLOOR:
                    unchanged += 1
                    continue
                num_occ = num_occupied_seen(puzzle_input, x, y)
                if puzzle_input[y][x] == EMPTY and num_occ == 0:
                    grid[y][x] = OCCUPIED
                elif puzzle_input[y][x] == OCCUPIED and num_occ >= 5:
                    grid[y][x] = EMPTY
                else:
                    unchanged += 1
        puzzle_input = deepcopy(grid)
    return count_occupied(grid)


a(puzzle_input)
b(puzzle_input)
