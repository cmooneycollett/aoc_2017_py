"""
Solutions for AOC 2017 Day 5.
"""


def process_input_file():
    """
    Processes the AOC 2017 Day 5 input file into the format required by the
    solver functions. Returned value is list of integers given in the input
    file.
    """
    with open("./input/day05.txt", encoding="utf-8") as file:
        return [int(line.strip()) for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(jumps):
    """
    Solves AOC 2017 Day 5 Part 1 // Returned value is the number of steps it
    takes to exit the list of jumps, where each jump that is executed is
    incremented by 1.
    """
    test_jumps = list(jumps)
    cursor = 0
    steps = 0
    while 0 <= cursor < len(test_jumps):
        old_cursor = cursor
        cursor += test_jumps[cursor]
        test_jumps[old_cursor] += 1
        steps += 1
    return steps


def solve_part2(_jumps):
    """
    Solves AOC 2017 Day 5 Part 2 // ###
    """
    return NotImplemented
