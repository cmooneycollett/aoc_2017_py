"""
Solutions for AOC 2017 Day 15.
"""

import re


class Generator:
    """
    Represents a number generator.
    """

    def __init__(self, seed, factor, check_function=lambda _: True):
        self.last_value = seed
        self.factor = factor
        self.check_function = check_function

    def next(self):
        """
        Yields the next value from the generator.
        """
        while True:
            output = self.last_value
            output *= self.factor
            output %= 2147483647
            self.last_value = output
            if self.check_function(output):
                break
        return self.last_value


def process_input_file(filepath="./input/day15.txt"):
    """
    Processes the AOC 2017 Day 15 input file into the format required by the
    solver functions. Returned value is list containing the seed values for the
    two number generators used in the day's problem.
    """
    seeds = []
    with open(filepath, encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            value = int(re.search(r"\d+", line).group())
            seeds.append(value)
    return seeds


def solve_part1(seeds):
    """
    Solves AOC 2017 Day 15 Part 1 // Calculates the judge's final score after
    40 million pairs generated from two generators using the given seeds.
    """
    gen1 = Generator(seeds[0], 16807)
    gen2 = Generator(seeds[1], 48271)
    judge_score = 0
    for _ in range(40000000):
        gen1_binchunk = bin(gen1.next())[-16:]
        gen2_binchunk = bin(gen2.next())[-16:]
        if gen1_binchunk == gen2_binchunk:
            judge_score += 1
    return judge_score


def solve_part2(seeds):
    """
    Solves AOC 2017 Day 15 Part 2 // Calculates the judge's final score after
    5 million pairs generated from two generators using the given seeds, where
    first generator looks for values that are multiples of 4 and the second
    generator looks for values that are multiples of 8.
    """
    gen1 = Generator(seeds[0], 16807, lambda n: n % 4 == 0)
    gen2 = Generator(seeds[1], 48271, lambda n: n % 8 == 0)
    judge_score = 0
    for _ in range(5000000):
        gen1_binchunk = bin(gen1.next())[-16:]
        gen2_binchunk = bin(gen2.next())[-16:]
        if gen1_binchunk == gen2_binchunk:
            judge_score += 1
    return judge_score
