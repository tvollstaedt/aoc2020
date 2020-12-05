from typing import List, Tuple


def part1(input: List[str], slope_x, slope_y):
    counter, x, y = [0, 0, 0]
    geo_map = [[ch for ch in list(line)] for line in input]
    while True:
        x += slope_x
        y += slope_y

        if y > len(geo_map) - 1:
            return counter
        if x > len(geo_map[y]) - 1:
            x -= len(geo_map[y])
        if geo_map[y][x] == "#":
            counter += 1


def part2(input: List[str], slopes: List[Tuple[int, int]]):
    amount = 1
    for slope_x, slope_y in slopes:
        amount *= part1(input, slope_x, slope_y)
    return amount
