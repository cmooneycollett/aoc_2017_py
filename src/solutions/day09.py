"""
Solutions for AOC 2017 Day 9.
"""


def process_input_file(filepath="./input/day09.txt"):
    """
    Processes the AOC 2017 Day 9 input file into the format required by the
    solver functions. Returned value is the string of characters given in the
    input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(char_stream):
    """
    Solves AOC 2017 Day 9 Part 1 // Returns the total score for all groups in
    the given character stream.
    """
    depth = 0   # tracks how many nested groups deep the cursor is
    score = 0   # tracks the running total score
    cursor = 0  # current index into the char stream
    in_garbage = False
    while cursor < len(char_stream):
        match char_stream[cursor]:
            case "{":
                if not in_garbage:
                    depth += 1
            case "}":
                if not in_garbage:
                    score += depth
                    depth -= 1
            case "<":
                # enter garbage
                in_garbage = True
            case ">":
                # exit garbage
                in_garbage = False
            case "!":
                # Skip next character if inside garbage
                if in_garbage:
                    cursor += 1
        cursor += 1
    return score


def solve_part2(char_stream):
    """
    Solves AOC 2017 Day 9 Part 2 // Counts the number of non-cancelled
    within the garbage of the given character stream.
    """
    garbage_char_count = 0
    cursor = 0
    in_garbage = False
    while cursor < len(char_stream):
        if in_garbage:
            garbage_char_count += 1
        match char_stream[cursor]:
            case "<":
                in_garbage = True
            case ">":
                in_garbage = False
                garbage_char_count -= 1
            case "!":
                cursor += 1
                garbage_char_count -= 1
        cursor += 1
    return garbage_char_count
