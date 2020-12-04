import sys
import re
from utils.log import log

puzzle_input = [x for x in sys.stdin.read().split('\n\n')]
puzzle_input = [x.split('\n') for x in puzzle_input]

hcl_regex = re.compile(r'#[0-9a-f]{6}')
ecl_regex = re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')


def validate_byr(s):
    (_, year) = s.split(':')
    year = int(year)
    return year >= 1920 and year <= 2002


def validate_iyr(s):
    (_, year) = s.split(':')
    year = int(year)
    return year >= 2010 and year <= 2020


def validate_eyr(s):
    (_, year) = s.split(':')
    year = int(year)
    return year >= 2020 and year <= 2030


def validate_hgt(s):
    (_, hgt) = s.split(':')
    (height, *split) = hgt.split('cm')
    if len(split) > 0:
        height = int(height)
        return height >= 150 and height <= 193
    (height, *split) = hgt.split('in')
    if len(split) > 0:
        height = int(height)
        return height >= 59 and height <= 76
    return False


def validate_hcl(s):
    (_, value) = s.split(':')
    return re.match(hcl_regex, value) != None


def validate_ecl(s):
    (_, value) = s.split(':')
    return re.match(ecl_regex, value) != None


def validate_pid(s):
    (_, value) = s.split(':')
    return len(value) == 9


def has_fields(s):
    if 'byr' in s and 'iyr' in s and 'eyr' in s and 'hgt' in s and 'hcl' in s and 'ecl' in s and 'pid' in s:
        return True


@log
def a(puzzle_input):
    num_valid = 0
    for s in puzzle_input:
        joined = ' '.join(s)
        if has_fields(joined):
            num_valid += 1
    return num_valid


@log
def b(puzzle_input):
    num_valid = 0
    for s in puzzle_input:
        joined = ' '.join(s)
        if has_fields(joined):
            key_value_pairs = sorted(
                filter(lambda s: not s.startswith('cid'), joined.split(' ')))
            (byr, ecl, eyr, hcl, hgt, iyr, pid) = key_value_pairs
            if validate_byr(byr) and validate_ecl(ecl) and validate_eyr(eyr) and validate_hcl(hcl) and validate_hgt(hgt) and validate_iyr(iyr) and validate_pid(pid):
                num_valid += 1
    return num_valid


a(puzzle_input)
b(puzzle_input)
