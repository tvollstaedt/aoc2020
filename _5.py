import math
from typing import List


def get_position(code: str, max_pos: int):
    pos_hi = max_pos
    pos_low = pos = 0
    for i in range(len(code)):
        if i == len(code) - 1 and (code[i] == "F" or code[i] == "L"):
            pos = pos_low
        elif i == len(code) - 1 and (code[i] == "B" or code[i] == "R"):
            pos = pos_hi
        if code[i] == "F" or code[i] == "L":
            pos_hi -= math.floor((pos_hi + 1 - pos_low) / 2)
        elif code[i] == "B" or code[i] == "R":
            pos_low += math.ceil((pos_hi + 1 - pos_low) / 2)
    return pos


def get_seat(code):
    row = get_position(code[:7], 127)
    col = get_position(code[-3:], 7)
    return row * 8 + col


def part1(input: List[str]):
    seat_hi = 0
    seat_low = 999

    for line in input:
        seat = get_seat(line)
        if seat_hi < seat:
            seat_hi = seat
        if seat_low > seat:
            seat_low = seat

    return seat_hi


def part2(input: List[str]):
    seats = set(range(11, 836))
    for line in input:
        seats.remove(get_seat(line))

    return seats.pop()
