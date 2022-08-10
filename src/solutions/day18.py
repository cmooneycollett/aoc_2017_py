"""
Solutions for AOC 2017 Day 18 - "Duet".
"""

from copy import deepcopy
from src.utils.machines.duet import SoundComputer


def process_input_file(filepath="./input/day18.txt"):
    """
    Processes the AOC 2017 Day 18 input file into the format required by the
    solver functions. Returned value is sound computer initialised with the
    instructions given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return SoundComputer(file.read().strip())


def solve_part1(sound_computer_initial):
    """
    Solves AOC 2017 Day 18 Part 1 // Determines the value of the recovered
    frequency the first time an "rcv" instruction is executed with a non-zero
    value.
    """
    sound_computer = deepcopy(sound_computer_initial)
    return sound_computer.execute_program()


def solve_part2(_sound_computer_initial):
    """
    Solves AOC 2017 Day 18 Part 2 // ###
    """
    return NotImplemented
