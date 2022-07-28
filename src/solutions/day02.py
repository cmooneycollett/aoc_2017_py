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


def solve_part2(rows):
    """
    Solves AOC 2017 Day 2 Part 2 // Determines the sum of each row's result
    value, which is result of the dvision for the only two numbers in the row
    which evenly divide into each other.
    """
    return sum(calculate_row_result(row) for row in rows)


def calculate_row_result(row):
    """
    Calculates the result of dividing the two values N and M from the given row,
    where N is evenly divisible by M.
    """
    # Check each value in row against all others (not including self)
    for (i_num, num) in enumerate(row):
        for (i_den, den) in enumerate(row):
            # Value is not compared against itself
            if i_num == i_den:
                continue
            # Add to the result sum if evenly divisible value pair found
            if num % den == 0:
                return num // den
    return -1
