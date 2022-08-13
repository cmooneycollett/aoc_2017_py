"""
Solutions for AOC 2017 Day 23 - "Coprocessor Conflagration".
"""

from copy import deepcopy
import math
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


def solve_part2(sound_computer_initial):
    """
    Solves AOC 2017 Day 23 Part 2 // Returns the value held in register "h" of
    SoundComputer after program execution halts, with debug switch toggled off.

    Optimised program counts the number of composite numbers (increasing by the
    step coded into the program - second-last instruction) between a lower and
    upper limit. The lower and upper limits are calculated based on the seed
    value coded in the first instruction of the program.
    """
    # Optimised execution of the sound computer code
    seed = abs(int(sound_computer_initial.get_instructions()[0][2]))
    step = abs(int(sound_computer_initial.get_instructions()[-2][2]))
    lower = seed * 100 + 100000
    upper = lower + 17000
    comp_count = 0
    for num in range(lower, upper + 1, step):
        if not is_prime(num):
            comp_count += 1
    return comp_count


def is_prime(num):
    """
    Checks if the given number is prime.
    """
    for val in range(2, int(math.sqrt(num)) + 1):
        if num % val == 0:
            return False
    return True
