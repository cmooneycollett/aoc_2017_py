"""
Solutions for AOC 2017 Day 14.
"""

from src.utils.cryptography import calculate_knot_hash


def process_input_file(filepath="./input/day14.txt"):
    """
    Processes the AOC 2017 Day 14 input file into the format required by the
    solver functions. Returned value is the key string given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(key):
    """
    Solves AOC 2017 Day 14 Part 1 // Calculates the number of used squares in
    the 128-by-128 disk grid using the given key string as seed for knot hashes
    for each row.
    """
    used_count = 0
    for row in range(128):
        knot_hash = calculate_knot_hash(f"{key}-{row}")
        used_count += bin(int(knot_hash, 16))[2:].count("1")
    return used_count


def solve_part2(_key):
    """
    Solves AOC 2017 Day 14 Part 2 // ###
    """
    return NotImplemented
