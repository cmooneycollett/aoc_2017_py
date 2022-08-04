"""
Solutions for AOC 2017 Day 12.
"""

from collections import deque
import re


def process_input_file(filepath="./input/day12.txt"):
    """
    Processes the AOC 2017 Day 12 input file into the format required by the
    solver functions. Returned value is dict containing the mapping of each
    program to the other programs it is connected to.
    """
    program_conns = {}
    regex_line = re.compile(r"^(\d+) <-> (.+)$")
    with open(filepath, encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if match_line := regex_line.match(line):
                program = int(match_line.group(1))
                conns = [int(conn) for conn in match_line.group(2).split(", ")]
                program_conns[program] = conns
    return program_conns


def solve_part1(program_conns):
    """
    Solves AOC 2017 Day 12 Part 1 // Calculates the number of programs that are
    in the group that contains program ID 0.
    """
    visit_queue = deque(program_conns[0])
    visited = set([0])
    while len(visit_queue) > 0:
        # Visit the next program
        program = visit_queue.popleft()
        visited.add(program)
        # Go to next programs not yet visited from current program
        for next_program in program_conns[program]:
            if next_program not in visited:
                visit_queue.append(next_program)
    return len(visited)


def solve_part2(_program_conns):
    """
    Solves AOC 2017 Day 12 Part 2 // ###
    """
    return NotImplemented
