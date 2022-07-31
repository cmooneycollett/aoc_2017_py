"""
Solutions for AOC 2017 Day 7.
"""

import re


def process_input_file(filepath="./input/day07.txt"):
    """
    Processes the AOC 2017 Day 7 input file into the format required by the
    solver functions. Returned value is tuple containing two dicts: the programs
    mapped to their weight, and the programs mapped to their children.
    """
    prog_weights = {}
    prog_children = {}
    regex_line = re.compile(r"^([a-z]+) \((\d+)\)(?: -> )?(.+)?$")
    with open(filepath, encoding="utf-8") as file:
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
    return determine_bottom_program(prog_children)


def solve_part2(program_data):
    """
    Solves AOC 2017 Day 7 Part 2 // Determines the correct weight of the one
    program in the overall tower that is at the incorrect weight.
    """
    (prog_weights, prog_children) = program_data
    prog_weights = dict(prog_weights)
    return find_corrected_program_weight(prog_weights, prog_children)


def find_corrected_program_weight(prog_weights, prog_children):
    """
    Determines the corrected weight for the one program with incorret weight.
    """
    bottom_prog = determine_bottom_program(prog_children)
    corrected_weight = []
    find_corrected_program_weight_recursive(prog_weights, prog_children,
                                            bottom_prog, corrected_weight)
    return corrected_weight[0]


def find_corrected_program_weight_recursive(prog_weights, prog_children,
                                            base_prog, corrected_weight):
    """
    Recursive method to process the program tree to find the program with
    incorrect weight and determine its correct weight.
    """
    # Stop processing the program tree if the corrected weight has been found
    if len(corrected_weight) >= 1:
        return -1
    # Tower weight is program weight if it has no children
    if len(prog_children[base_prog]) == 0:
        return prog_weights[base_prog]
    # Find weights of children
    child_weights = {}
    for child in prog_children[base_prog]:
        child_weights[child] = find_corrected_program_weight_recursive(
            prog_weights, prog_children, child, corrected_weight)
    # Check the balance of the child weights
    occurences = {}
    for weight in child_weights.values():
        if weight in occurences:
            occurences[weight] += 1
        else:
            occurences[weight] = 1
    if len(occurences) == 1:
        return sum(child_weights.values()) + prog_weights[base_prog]
    # Determine which program has the invalid weight
    valid_weight = max(occurences, key=occurences.get)
    invalid_prog = ""
    invalid_weight = -1
    for (prog, weight) in child_weights.items():
        if weight != valid_weight:
            invalid_prog = prog
            invalid_weight = weight
            break
    # Determine the correct weight for the program with invalid weight
    correct_weight = valid_weight - (invalid_weight -
                                     prog_weights[invalid_prog])
    corrected_weight.append(correct_weight)
    return -1


def determine_bottom_program(prog_children):
    """
    Determines the bottom program, by finding the only program that is not a
    child of another program.
    """
    progs_set = set(prog_children.keys())   # All unique programs
    children_set = set()    # All unique children programs
    for children in prog_children.values():
        children_set.update(children)
    # Bottom program is the only program that is not a child to another program
    return (progs_set - children_set).pop()
