import sys
import math
from utils.log import log

puzzle_input = [x for x in sys.stdin.read().split('\n')]

def direction_to_delta(direction):
    if direction == "E":
        return (1, 0)
    elif direction == "S":
        return (0, 1)
    elif direction == "W":
        return (-1, 0)
    else:
        return (0, -1)

def heading_to_delta(heading):
    h = heading % 360
    if h == 0:
        return (1, 0)
    elif h == 90:
        return (0, 1)
    elif h == 180:
        return (-1, 0)
    else:
        return (0, -1)

heading = 0

@log
def a(puzzle_input):
    x, y = 0, 0
    heading = 0
    for i in puzzle_input:
        instruction, distance = i[0], i[1:]
        distance = int(distance)
        if instruction == 'R':
            heading += distance
        elif instruction == 'L':
            heading -= distance
        elif instruction == 'F':
            x_delta, y_delta = heading_to_delta(heading)
            x += x_delta * distance
            y += y_delta * distance
        else:
            x_delta, y_delta = direction_to_delta(instruction)
            x += x_delta * distance
            y += y_delta * distance
    return abs(x) + abs(y)
            
def rotate_waypoint(instruction, x, y):
    if instruction == "R":
        return (-y, x)
    return (y, -x)

@log
def b(puzzle_input):
    x, y = 0, 0
    heading = 0
    waypoint_x, waypoint_y = 10, -1
    for i in puzzle_input:
        instruction, distance = i[0], i[1:]
        distance = int(distance)
        if instruction == 'R' or instruction == 'L':
            num_turns = distance // 90
            for _ in range(num_turns):
                waypoint_x, waypoint_y = rotate_waypoint(instruction, waypoint_x, waypoint_y)
        elif instruction == 'F':
            x_delta, y_delta = heading_to_delta(heading)
            x +=  distance * waypoint_x
            y +=  distance * waypoint_y
        else:
            x_delta, y_delta = direction_to_delta(instruction)
            waypoint_x += x_delta * distance
            waypoint_y += y_delta * distance
    return abs(x) + abs(y)


a(puzzle_input)
b(puzzle_input)
