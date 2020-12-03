import sys
import re
from utils.log import log

puzzle_input = [x for x in sys.stdin.read().split('\n')]

regex = re.compile(r'(\d+)-(\d+)\s([a-z]):\s([a-z]+)')

def count_letter(l, s):
    num = 0
    for c in s:
        if c == l:
            num += 1
    return num

@log
def a(puzzle_input):
    valid_pws = 0
    for s in puzzle_input:
        (least, most, letter, pw) = re.search(regex, s).groups()
        count = count_letter(letter, pw)
        if count >= int(least) and count <= int(most):
            valid_pws += 1
    return valid_pws


def validate(p1, p2, letter, password):
    p1, p2 = p1 - 1, p2 - 1
    if password[p1] == letter and password[p2] != letter:
        return True
    if password[p2] == letter and password[p1] != letter:
        return True
    if password[p1] == letter and password[p2] == letter:
        return False
    if password[p1] == letter or password[p2] == letter:
        return True
    return False

@log
def b(puzzle_input):
    valid_pws = 0
    for s in puzzle_input:
        (pos1, pos2, letter, pw) = re.search(regex, s).groups()
        if validate(int(pos1), int(pos2), letter, pw):
            valid_pws += 1
    return valid_pws


a(puzzle_input)
b(puzzle_input)
