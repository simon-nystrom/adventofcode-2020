import sys
from utils.log import log

puzzle_input = [x.split(' ') for x in sys.stdin.read().split('\n')]

instructions = {}
for i, instruction in enumerate(puzzle_input):
    op, val = instruction
    val = int(val)
    instructions[i] = (op, val)


def execute(pc, acc):
    new_pc, new_acc = pc, acc
    op, val = instructions[new_pc]
    if op == 'acc':
        new_acc += val
    elif op == 'jmp':
        # Jump 1 less than intended to adjust for addition of 1 in return statement
        new_pc += val - 1
    return new_pc + 1, new_acc


@log
def a(puzzle_input):
    pc, acc = 0, 0
    executed_rows = {}
    while not pc in executed_rows:
        executed_rows[pc] = True
        pc, acc = execute(pc, acc)
    return acc


def toggle(instr):
    if instr == 'acc':
        return 'acc'
    if instr == 'nop':
        return 'jmp'
    return 'nop'


@log
def b(puzzle_input):
    for i, instruction in enumerate(instructions.values()):
        op, dist = instruction
        instructions[i] = (toggle(op), dist)
        pc, acc = 0, 0
        executed_rows = {}
        while not pc in executed_rows:
            executed_rows[pc] = True
            pc, acc = execute(pc, acc)
            if pc == len(instructions):
                return acc
        # Restore original instruction
        instructions[i] = instruction


a(puzzle_input)
b(puzzle_input)
