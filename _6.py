import string
from typing import List


def part1(input: List[str]):
    counter = 0
    for group in input:
        counter += len(set(group.replace("\n", "")))
    return counter


def part2(input: List[str]):
    counter = 0
    for group in input:
        group_answers = set(string.ascii_lowercase)
        for person_answers in filter(None, group.split("\n")):
            group_answers = set(person_answers).intersection(group_answers)
        counter += len(group_answers)
    return counter
