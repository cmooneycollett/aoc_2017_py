"""
Solutions for AOC 2017 Day 25 = "The Halting Problem".
"""

from collections import deque
import re


def process_input_file(filepath="./input/day25.txt"):
    """
    Processes the AOC 2017 Day 25 input file into the format required by the
    solver functions. Returns tuple containing the start state, number of steps
    to conduct and the state instructions.
    """
    with open(filepath, encoding="utf-8") as file:
        regex_header = \
            r"Begin in state ([A-Z]).\n" \
            r"Perform a diagnostic checksum after (\d+) steps."
        regex_state = \
            r"In state ([A-Z]):\n" \
            r"  If the current value is 0:\n" \
            r"    - Write the value (\d).\n" \
            r"    - Move one slot to the (left|right).\n" \
            r"    - Continue with state ([A-Z]).\n" \
            r"  If the current value is 1:\n" \
            r"    - Write the value (\d).\n" \
            r"    - Move one slot to the (left|right).\n" \
            r"    - Continue with state ([A-Z])."
        raw_input = file.read().strip()
        match_header = re.search(regex_header, raw_input)
        state_instructions = {}
        start_state = match_header.group(1)
        steps = int(match_header.group(2))
        for mstate in re.findall(regex_state, raw_input):
            state_instructions[mstate[0]] = {
                0: (int(mstate[1]), mstate[2] == "right", mstate[3]),
                1: (int(mstate[4]), mstate[5] == "right", mstate[6])
            }
        return (start_state, steps, state_instructions)


def solve_part1(turing_config):
    """
    Solves AOC 2017 Day 25 Part 1 // Determines the diagnostic checksum of the
    Turing machine (number of "1" symbols on the tape) when it has completed
    the specified number of steps.
    """
    (state, steps, state_instructions) = turing_config
    tape = deque([0])
    cursor = 0
    for _ in range(steps):
        (val, move_right, next_state) = state_instructions[state][tape[cursor]]
        # Update tape value
        tape[cursor] = val
        # Move the cursor
        if move_right:  # move cursor to the left
            if cursor == len(tape) - 1:
                tape.append(0)
            cursor += 1
        else:   # move cursor to the right
            if cursor == 0:
                tape.appendleft(0)
            else:
                cursor -= 1
        # Update Turing machine state
        state = next_state
    return tape.count(1)


def solve_part2(_turing_config):
    """
    Solves AOC 2017 Day 25 Part 2 // The printer has been rebooted and Christmas
    is saved!
    """
    return True
