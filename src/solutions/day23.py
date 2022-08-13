"""
Solutions for AOC 2017 Day 23 - "Coprocessor Conflagration".
"""

from copy import deepcopy
from src.utils.machines.duet import SoundComputer


def process_input_file(filepath="./input/day23.txt"):
    """
    Processes the AOC 2017 Day 23 input file into the format required by the
    solver functions. Returns a SoundComputer loaded with the instructions
    given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return SoundComputer(file.read().strip())


def solve_part1(sound_computer_initial):
    """
    Solves AOC 2017 Day 23 Part 1 // Returns the number of times the "mul"
    instruction is executed by the SoundComputer.
    """
    sound_computer = deepcopy(sound_computer_initial)
    sound_computer.execute_program()
    return sound_computer.get_execution_count_mul()


def solve_part2(_sound_computer_initial):
    """
    Solves AOC 2017 Day 23 Part 2 // ###
    """
    return NotImplemented
