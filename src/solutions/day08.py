"""
Solutions for AOC 2017 Day 8.
"""

from dataclasses import dataclass
from enum import Enum, unique
import re


@unique
class Operator(Enum):
    """
    Represents the different operators that occur in the value checking
    expressions.
    """
    GT = ">"    # greater than
    GEQ = ">="  # greater than or equal to
    EQ = "=="   # equal
    LT = "<"    # less than
    LEQ = "<="  # less than or equal to
    NEQ = "!="  # not equal to


@dataclass
class Instruction:
    """
    Represents a single instruction.
    """
    target_reg: str     # register to be operated on
    is_increment: bool  # increment operation if true, decrement if false
    value: int          # value to increase or decrease target register by
    check_reg: str      # register whose value is checked
    operator: Operator  # operator used to check register
    check_value: int    # value against which register value is checked


def process_input_file(filepath="./input/day08.txt"):
    """
    Processes the AOC 2017 Day 8 input file into the format required by the
    solver functions. ###
    """
    instruction_regex = re.compile(
        r"^([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) (>|>=|==|<|<=|!=) (-?\d+)$")
    instructions = []
    with open(filepath, encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if match_instruction := instruction_regex.match(line):
                target_reg = match_instruction.group(1)
                is_increment = (match_instruction.group(2) == "inc")
                value = int(match_instruction.group(3))
                check_reg = match_instruction.group(4)
                operator = Operator(match_instruction.group(5))
                check_value = int(match_instruction.group(6))
                instructions.append(
                    Instruction(target_reg, is_increment, value, check_reg,
                                operator, check_value))
    return instructions


def solve_part1(instructions):
    """
    Solves AOC 2017 Day 8 Part 1 // Returns the largest value in any register
    after executing all of the given instructions.
    """
    (max_at_end, _) = evaluate_instructions(instructions)
    return max_at_end


def solve_part2(instructions):
    """
    Solves AOC 2017 Day 8 Part 2 // Returns the largest value observed in a
    register at any point during execution.
    """
    (_, max_during) = evaluate_instructions(instructions)
    return max_during


def evaluate_instructions(instructions):
    """
    Evalues the given instructions, returning tuple containing the maximum value
    in register at end of execution and maximum value in register at any point
    throughout execution.
    """
    regs = {}   # Registers initialised to 0 when first encountered
    max_value = 0
    for instruct in instructions:
        # Add registers to the bank if not already seen
        if instruct.target_reg not in regs:
            regs[instruct.target_reg] = 0
        if instruct.check_reg not in regs:
            regs[instruct.check_reg] = 0
        # Evaluate the check expression
        check_exp = False
        match instruct.operator:
            case Operator.GT:
                check_exp = (regs[instruct.check_reg] > instruct.check_value)
            case Operator.GEQ:
                check_exp = (regs[instruct.check_reg] >= instruct.check_value)
            case Operator.EQ:
                check_exp = (regs[instruct.check_reg] == instruct.check_value)
            case Operator.LT:
                check_exp = (regs[instruct.check_reg] < instruct.check_value)
            case Operator.LEQ:
                check_exp = (regs[instruct.check_reg] <= instruct.check_value)
            case Operator.NEQ:
                check_exp = (regs[instruct.check_reg] != instruct.check_value)
        # Update target regiter value if check expression is true
        if check_exp:
            if instruct.is_increment:
                regs[instruct.target_reg] += instruct.value
            else:
                regs[instruct.target_reg] -= instruct.value
            # Check if new maximum register value seen
            if regs[instruct.target_reg] > max_value:
                max_value = regs[instruct.target_reg]
    return (max(regs.values()), max_value)
