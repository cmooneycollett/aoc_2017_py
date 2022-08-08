"""
Solutions for AOC 2017 Day 17.
"""


def process_input_file(filepath="./input/day17.txt"):
    """
    Processes the AOC 2017 Day 17 input file into the format required by the
    solver functions. Returns the step count given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return int(file.read().strip())


def solve_part1(steps):
    """
    Solves AOC 2017 Day 17 Part 1 // Returns the value after the value 2017 in
    the spinlock.
    """
    spinlock = [0]
    cursor = 0
    for code in range(1, 2018):
        print(f"[+] Inserted code {code} at index {cursor + 1}")
        spinlock.insert(cursor + 1, code)
        cursor = (cursor + 1 + steps) % len(spinlock)
    target_index = (spinlock.index(2017) + 1) % len(spinlock)
    return spinlock[target_index]


def solve_part2(_steps):
    """
    Solves AOC 2017 Day 17 Part 2 // ###
    """
    return NotImplemented
