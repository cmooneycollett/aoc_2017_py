"""
Solutions for AOC 2017 Day 1.
"""


def process_input_file():
    """
    Processes the AOC 2017 Day 1 input file into the format required by the
    solver functions. Returned value is the captcha string given in the input
    file.
    """
    with open("./input/day01.txt", encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(captcha):
    """
    Solves AOC 2017 Day 1 Part 1 // Determines the result of processing the
    given captcha where the pair character considered is the following character
    in the captcha (circular).
    """
    total = 0
    for (index, char) in enumerate(captcha):
        target = (index + 1) % len(captcha)
        if char == captcha[target]:
            total += int(char)
    return total


def solve_part2(captcha):
    """
    Solves AOC 2017 Day 1 Part 2 // Determines the result of processing the
    given captcha where the pair character considered is haly-way along the
    captcha from each character (circular).
    """
    total = 0
    for (index, char) in enumerate(captcha):
        target = (index + len(captcha) // 2) % len(captcha)
        if char == captcha[target]:
            total += int(char)
    return total
