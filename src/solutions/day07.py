"""
Solutions for AOC 2017 Day 7.
"""

import re


def process_input_file():
    """
    Processes the AOC 2017 Day 7 input file into the format required by the
    solver functions. Returned value is tuple containing two dicts: the programs
    mapped to their weight, and the programs mapped to their children.
    """
    prog_weights = {}
    prog_children = {}
    regex_line = re.compile(r"^([a-z]+) \((\d+)\)(?: -> )?(.+)?$")
    with open("./input/day07.txt", encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if match_line := regex_line.match(line):
                prog = match_line.group(1)
                weight = int(match_line.group(2))
                children = []
                if match_line.group(3):
                    children = match_line.group(3).split(", ")
                prog_weights[prog] = weight
                prog_children[prog] = children
    return (prog_weights, prog_children)


def solve_part1(program_data):
    """
    Solves AOC 2017 Day 7 Part 1 // Determines the name of the program at the
    bottom of the tower.
    """
    (_, prog_children) = program_data
    progs_set = set(prog_children.keys())   # All unique programs
    children_set = set()    # All unique children programs
    for children in prog_children.values():
        children_set.update(children)
    # Bottom program is the only program that is not a child to another program
    return (progs_set - children_set).pop()


def solve_part2(_program_data):
    """
    Solves AOC 2017 Day 7 Part 2 // ###
    """
    return NotImplemented
