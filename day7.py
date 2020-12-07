import sys
import re
from utils.log import log

puzzle_input = [x for x in sys.stdin.read().split('\n')]

bag_color_regex = re.compile(r'(\w+ \w+)')
num_inside_bags_regex = re.compile(r'(\d+ \w+ \w+)')

bags = {}
# Build graph
for s in puzzle_input:
    color = bag_color_regex.match(s).group(1)
    num_bags = num_inside_bags_regex.findall(s)
    if not color in bags:
        bags[color] = {}
    for num in num_bags:
        num, *desc = num.split(" ")
        desc = " ".join(desc)
        if not desc in bags[color]:
            bags[color][desc] = {}
        bags[color][desc] = int(num)


def can_contain(source, target):
    if source == target:
        return True
    return any([can_contain(bag, target) for bag in bags[source].keys()])

@log
def a(puzzle_input):
    total = 0
    for key in bags.keys():
        if can_contain(key, 'shiny gold'):
            total += 1
    # Subtract 1 to remove shiny gold bag itself from the count
    return total - 1


def count(source, total=0):
    total = sum(bags[source].values())
    for desc, num in bags[source].items():
        total += num * count(desc, total)
    return total


@log
def b(puzzle_input):
    return count('shiny gold')


a(puzzle_input)
b(puzzle_input)
