"""
Solutions for AOC 2017 Day 6.
"""


def process_input_file():
    """
    Processes the AOC 2017 Day 6 input file into the format required by the
    solver functions. Returned value is the list representing the initial state
    of the memory banks given in the input file.
    """
    with open("./input/day06.txt", encoding="utf-8") as file:
        return tuple(int(bank) for bank in file.read().strip().split())


def solve_part1(membanks_initial):
    """
    Solves AOC 2017 Day 6 Part 1 // Determines the number of redistribution
    cycles that must be completed before a configuration is produced that has
    been seen before.
    """
    membanks = tuple(membanks_initial)
    seen = set([membanks])
    while True:
        # Perform redistribution cycle
        membanks = redistribute_membanks(membanks)
        # Check if configuration has been seen before
        if membanks in seen:
            break
        seen.add(membanks)
    return len(seen)


def redistribute_membanks(membanks):
    """
    Redistributes the membanks by taking the blocks from the bank with the
    largest number and redistributing them one-by-one to subsequent blocks
    (circular around the list).
    """
    new_membanks = list(membanks)
    cursor = new_membanks.index(max(new_membanks))
    blocks = new_membanks[cursor]
    new_membanks[cursor] = 0
    while blocks > 0:
        cursor = (cursor + 1) % len(new_membanks)
        new_membanks[cursor] += 1
        blocks -= 1
    return tuple(new_membanks)


def solve_part2(_membanks_initial):
    """
    Solves AOC 2017 Day 6 Part 2 // ###
    """
    return NotImplemented
