import re
from typing import List

must_match = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def part1(input: List[str]):
    counter = 0
    for line in input:
        line = line.replace("\n", " ")
        entry_fields = set([attributes.split(":")[0] for attributes in line.split(" ")])

        if must_match.issubset(entry_fields):
            counter += 1
    return counter


def part2(input: List[str]):
    attribute_value_matchers = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': lambda v: 150 <= int(v[:-2]) <= 193 if "cm" in v else 59 <= int(v[:-2]) <= 79,
        'hcl': lambda v: re.search("^#[0-9a-f]{6}$", v),
        'ecl': lambda v: v in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        'pid': lambda v: re.search("^[0-9]{9}$", v),
        'cid': lambda v: True
    }

    counter = 0

    for line in input:
        line = line.replace("\n", " ")
        entry_fields = set([attributes.split(":")[0] for attributes in line.split(" ")])
        all_valid = must_match.issubset(entry_fields)  # Required fields present?

        if all_valid:  # Good, lets check the values of each field
            for attributes in line.strip().split(" "):
                key, value = attributes.strip().split(":")
                all_valid = attribute_value_matchers.get(key, lambda v: False)(value)

                if not all_valid:
                    break

        if all_valid:  # Still all valid, increase counter
            counter += 1

    return counter
