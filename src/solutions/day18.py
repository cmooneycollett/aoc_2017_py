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
    sound_computer.execute_program()
    return sound_computer.get_last_played_sound()


def solve_part2(sound_computer_initial):
    """
    Solves AOC 2017 Day 18 Part 2 // Determines the total number of sounds sent
    by program 1, when the sound computer is operated as two machines running
    in duet mode.
    """
    comp0 = deepcopy(sound_computer_initial)
    comp0.set_register("p", 0)
    comp0.set_duet_mode(True)
    comp1 = deepcopy(sound_computer_initial)
    comp1.set_register("p", 1)
    comp1.set_duet_mode(True)
    while True:
        # Check for halting conditions
        if comp0.is_halted() and comp1.is_halted():
            break
        if comp0.is_halted() and comp1.is_awaiting_input():
            break
        if comp0.is_awaiting_input() and comp1.is_awaiting_input():
            break
        # Execute programs
        comp0.execute_program()
        comp1.execute_program()
        # Send and receive sounds
        if comp0.is_awaiting_input():
            sounds = comp1.get_sent_sounds()
            comp0.receive_sounds(sounds)
        if comp1.is_awaiting_input():
            sounds = comp0.get_sent_sounds()
            comp1.receive_sounds(sounds)
    return comp1.get_total_sounds_sent()
