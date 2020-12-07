import sys
from utils.log import log

puzzle_input = [x for x in sys.stdin.read().split('\n\n')]
puzzle_input = [x.split('\n') for x in puzzle_input]


@log
def a(puzzle_input):
    total = 0
    answers = []
    for group in puzzle_input:
        a = set()
        for person in group:
            for answer in person:
                a.add(answer)
        answers.append(a)
    for answer in answers:
        total += len(answer)
    return total


@log
def b(puzzle_input):
    total = 0
    for group in puzzle_input:
        num_people = 0
        num_answers_by_question = {}
        for person in group:
            num_people += 1
            for answer in person:
                if not answer in num_answers_by_question:
                    num_answers_by_question[answer] = 1
                else:
                    num_answers_by_question[answer] += 1
        for num_answers in num_answers_by_question.values():
            if num_people == num_answers:
                total += 1
    return total


a(puzzle_input)
b(puzzle_input)
