"""
Solutions for AOC 2017 Day 6.
"""


def process_input_file(filepath="./input/day06.txt"):
    """
    Processes the AOC 2017 Day 6 input file into the format required by the
    solver functions. Returned value is the list representing the initial state
    of the memory banks given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return tuple(int(bank) for bank in file.read().strip().split())


def solve_part1(membanks_initial):
    """
    Solves AOC 2017 Day 6 Part 1 // Determines the number of redistribution
    cycles that must be completed before a configuration is produced that has
    been seen before.
    """
    (_, seen) = find_first_repeated_configuration(membanks_initial)
    return len(seen)


def solve_part2(membanks_initial):
    """
    Solves AOC 2017 Day 6 Part 2 // Determines the size of the infinite loop of
    configurations that arises from the given initial configuration of memory
    banks.
    """
    (membanks_repeat, _) = find_first_repeated_configuration(membanks_initial)
    membanks = tuple(membanks_repeat)
    steps = 0
    while True:
        steps += 1
        membanks = redistribute_membanks(membanks)
        if membanks == membanks_repeat:
            break
    return steps


def find_first_repeated_configuration(membanks_initial):
    """
    Determines the first memory bank configuration that is repeated by
    conducting successive redistribution cycles starting with the given initial
    memory bank state. Returned value is tuple containing the repeated
    configuration and the previously seen configurations.
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
    return (membanks, seen)


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
