"""
Solutions for AOC 2017 Day 4.
"""

import itertools


def process_input_file(filepath="./input/day04.txt"):
    """
    Processes the AOC 2017 Day 4 input file into the format required by the
    solver functions. Returned value is list containings lists for each line
    with the words on each line of the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return [line.strip().split() for line in file.readlines()
                if len(line.strip()) > 0]


def solve_part1(passphrases):
    """
    Solves AOC 2017 Day 4 Part 1 // Returns the number of valid passphrases,
    where valid passphrases contain no duplicate words.
    """
    return len([row for row in passphrases if len(set(row)) == len(row)])


def solve_part2(passphrases):
    """
    Solves AOC 2017 Day 4 Part 2 // Returns the number of valid passphrases,
    where valid passphrases contain no two words that are anagrams of each
    other.
    """
    return len([row for row in passphrases if not check_for_anagrams(row)])


def check_for_anagrams(passphrase):
    """
    Checks if the given passphrases contains two words that are anagrams of each
    other.
    """
    for (cursor, word) in enumerate(passphrase):
        # Use only unique orderings in case word contains duplicate letters
        ords = set("".join(ord) for ord in itertools.permutations(word))
        # Passphrase is invalid if it contains another word in the current ords
        for (check_cursor, check_word) in enumerate(passphrase):
            if cursor == check_cursor:
                break
            if check_word in ords:
                return True
    return False
