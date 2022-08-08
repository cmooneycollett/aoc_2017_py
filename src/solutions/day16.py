"""
Solutions for AOC 2017 Day 16.
"""

from collections import deque
from enum import Enum, auto, unique
import re


@unique
class DanceMove(Enum):
    """
    Represents the three different dance moves that can be conducted by the
    programs observed in the AOC 2017 Day 16 problem.
    """
    SPIN = auto()
    EXCHANGE = auto()
    PARTNER = auto()


def process_input_file(filepath="./input/day16.txt"):
    """
    Processes the AOC 2017 Day 16 input file into the format required by the
    solver functions. Returns a list containing the dance moves given as
    comma-separated units in the input file.
    """
    regex_spin = re.compile(r"^s(\d+)$")
    regex_exchange = re.compile(r"^x(\d+)/(\d+)$")
    regex_partner = re.compile(r"^p([a-p])/([a-p])$")
    dance_moves = []
    with open(filepath, encoding="utf-8") as file:
        for move in file.read().strip().split(","):
            if match_spin := regex_spin.match(move):
                dance_moves.append((DanceMove.SPIN, int(match_spin.group(1))))
            elif match_exchange := regex_exchange.match(move):
                dance_moves.append((DanceMove.EXCHANGE, int(match_exchange.group(1)),
                                    int(match_exchange.group(2))))
            elif match_partner := regex_partner.match(move):
                dance_moves.append((DanceMove.PARTNER, match_partner.group(1),
                                    match_partner.group(2)))
    return dance_moves


def solve_part1(dance_moves):
    """
    Solves AOC 2017 Day 16 Part 1 // Determines the order of the programs "a"
    through "p" after they have finished their dance.
    """
    return conduct_dance("abcdefghijklmnop", dance_moves)


def solve_part2(_dance_moves):
    """
    Solves AOC 2017 Day 16 Part 2 // ###
    """
    return NotImplemented


def conduct_dance(start_programs, dance_moves):
    """
    Operates on the order of the given programs (string) using the dance moves,
    returning the order of the programs when the dance is finished.
    """
    programs = deque(start_programs)
    for move in dance_moves:
        match move[0]:
            case DanceMove.SPIN:
                (_, steps) = move
                for _ in range(steps):
                    programs.appendleft(programs.pop())
            case DanceMove.EXCHANGE:
                (_, index1, index2) = move
                prog1 = programs[index1]
                prog2 = programs[index2]
                programs[index1] = prog2
                programs[index2] = prog1
            case DanceMove.PARTNER:
                (_, prog1, prog2) = move
                index1 = programs.index(prog1)
                index2 = programs.index(prog2)
                programs[index1] = prog2
                programs[index2] = prog1
    return "".join(programs)
