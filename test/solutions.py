"""
This module contains the test methods used to test the actual solutions for
each of the solved AOC 2017 problem parts. Test methods utilising pytest
library.
"""

from src.solutions import day01

def test_day01_part1():
    """
    Solution test method for AOC 2017 Day 1 Part 1.
    """
    input_data = day01.process_input_file()
    solution = day01.solve_part1(input_data)
    assert solution == 1150