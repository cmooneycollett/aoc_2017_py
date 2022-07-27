"""
This module contains the runner methods used to run the solved solutions and
print out the results.
"""


def solve_day_01():
    """
    Solves AOC 2017 Day 1 Parts 1 and 2, printing out the solutions.
    """
    print("AOC 2017 Day 1 - \"Inverse Captcha\"")
    input_data = day01.process_input_file()
    p1_solution = day01.solve_part1(input_data)
    print(f"> P1 solution - {p1_solution}")
    p2_solution = day01.solve_part2(input_data)
    print(f"> P2 solution - {p2_solution}")
    print("==========")


if __name__ == "__main__":
    # Import to allow execution from project top-level directory
    import os
    import sys
    sys.path.append(os.getcwd())
    # Solution module imports
    from src.solutions import day01
    # Main solver methods
    print("==========")
    solve_day_01()
