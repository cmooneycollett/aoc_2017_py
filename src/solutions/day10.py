"""
Solutions for AOC 2017 Day 10.
"""

from src.utils.cryptography import calculate_knot_hash, calculate_sparse_hash


def process_input_file(filepath="./input/day10.txt"):
    """
    Processes the AOC 2017 Day 10 input file into the format required by the
    solver functions. Returned value is string of comma-separated values given
    in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_string):
    """
    Solves AOC 2017 Day 10 Part 1 // Returns the product of first two numbers in
    list, initialised with values 0 to 255 in sequence, after applying the knot
    hash algorithm for the given number of lengths.
    """
    lengths = [int(num) for num in input_string.split(",")]
    (strand, _, _) = calculate_sparse_hash(list(range(256)), lengths)
    return strand[0] * strand[1]


def solve_part2(input_string):
    """
    Solves AOC 2017 Day 10 Part 2 // Calculates the knot hash for the given
    string.
    """
    return calculate_knot_hash(input_string)
