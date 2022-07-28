"""
Solutions for AOC 2017 Day 2.
"""


def process_input_file():
    """
    Processes the AOC 2017 Day 2 input file into the format required by the
    solver functions. Returned value is list containing each row of numbers
    as a list, given in input file as tab-separated values.
    """
    with open("./input/day02.txt", encoding="utf-8") as file:
        return [[int(value) for value in line.strip().split()]
                for line in file.readlines() if len(line.strip()) > 0]


def solve_part1(rows):
    """
    Solves AOC 2017 Day 2 Part 1 // Calculates the checksum for the given rows
    as the sum for all rows of the difference between each rows largest and
    smallest values.
    """
    checksum = 0
    for row in rows:
        checksum += max(row) - min(row)
    return checksum


def solve_part2(_rows):
    """
    Solves AOC 2017 Day 2 Part 2 // ###
    """
    return NotImplemented
