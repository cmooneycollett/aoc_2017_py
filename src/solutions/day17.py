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
        spinlock.insert(cursor + 1, code)
        cursor = (cursor + 1 + steps) % len(spinlock)
    target_index = (spinlock.index(2017) + 1) % len(spinlock)
    return spinlock[target_index]


def solve_part2(steps):
    """
    Solves AOC 2017 Day 17 Part 2 // Returns the value after the value 0 the
    moment that the value 50000000 is inserted.
    """
    cap = 50000000      # Stop after 50 million "inserts" into spinlock
    cursor = 0          # Track the insert location by cursor
    spinlock_len = 1    # spinlock length matters, but not all values
    last_code_after_zero = 0
    for code in range(1, cap + 1):
        # Check if a new value is inserted after 0, which is always be cursor 0
        if cursor == 0:
            last_code_after_zero = code
        spinlock_len += 1
        cursor = (cursor + 1 + steps) % spinlock_len
    return last_code_after_zero
