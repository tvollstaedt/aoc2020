from typing import List


def part1(input: List[str]):
    for i in input:
        for j in input:
            if int(i) + int(j) == 2020:
                return int(i) * int(j)
    return 0


def part2(input: List[str]):
    for i in input:
        for j in input:
            for k in input:
                if int(i) + int(j) + int(k) == 2020:
                    return int(i) * int(j) * int(k)
    return 0
