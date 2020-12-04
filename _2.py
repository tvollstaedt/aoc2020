from typing import List


def part1(input: List[str]):
    counter = 0
    for line in input:
        occurrence, char, password = line.split()
        min_occurrence, max_occurrence = occurrence.split("-")
        if int(min_occurrence) <= password.count(char[-2]) <= int(max_occurrence):
            counter += 1

    return counter


def part2(input: List[str]):
    counter = 0
    for line in input:
        occurrence, char, password = line.split()
        first_occurrence, second_occurrence = occurrence.split("-")

        if (password[int(first_occurrence) - 1] == char[-2]) ^ (password[int(second_occurrence) - 1] == char[-2]):
            counter += 1

    return counter
