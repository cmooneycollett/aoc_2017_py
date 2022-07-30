"""
Solutions for AOC 2017 Day 4.
"""


def process_input_file():
    """
    Processes the AOC 2017 Day 4 input file into the format required by the
    solver functions. Returned value is list containings lists for each line
    with the words on each line of the input file.
    """
    with open("./input/day04.txt", encoding="utf-8") as file:
        return [line.strip().split() for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(passphrases):
    """
    Solves AOC 2017 Day 4 Part 1 // Returns the number of valid passphrases,
    where valid passphrases contain no duplicate words.
    """
    return len([row for row in passphrases if len(set(row)) == len(row)])


def solve_part2(_passphrases):
    """
    Solves AOC 2017 Day 4 Part 2 // ###
    """
    return NotImplemented
