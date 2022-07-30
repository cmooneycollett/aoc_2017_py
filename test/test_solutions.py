"""
This module contains the test methods used to test the actual solutions for
each of the solved AOC 2017 problem parts. Test methods utilising pytest
library.
"""

from src.solutions import day01, day02, day03, day04


def test_day01_part1():
    """
    Solution test method for AOC 2017 Day 1 Part 1.
    """
    input_data = day01.process_input_file()
    solution = day01.solve_part1(input_data)
    assert solution == 1150


def test_day01_part2():
    """
    Solution test method for AOC 2017 Day 1 Part 1.
    """
    input_data = day01.process_input_file()
    solution = day01.solve_part2(input_data)
    assert solution == 1064


def test_day02_part1():
    """
    Solution test method for AOC 2017 Day 2 Part 1.
    """
    input_data = day02.process_input_file()
    solution = day02.solve_part1(input_data)
    assert solution == 45158


def test_day02_part2():
    """
    Solution test method for AOC 2017 Day 2 Part 2.
    """
    input_data = day02.process_input_file()
    solution = day02.solve_part2(input_data)
    assert solution == 294


def test_day03_part1():
    """
    Solution test method for AOC 2017 Day 3 Part 1.
    """
    input_data = day03.process_input_file()
    solution = day03.solve_part1(input_data)
    assert solution == 480


def test_day03_part2():
    """
    Solution test method for AOC 2017 Day 3 Part 2.
    """
    input_data = day03.process_input_file()
    solution = day03.solve_part2(input_data)
    assert solution == 349975


def test_day04_part1():
    """
    Solution test method for AOC 2017 Day 4 Part 1.
    """
    input_data = day04.process_input_file()
    solution = day04.solve_part1(input_data)
    assert solution == 386


def test_day04_part2():
    """
    Solution test method for AOC 2017 Day 4 Part 2.
    """
    input_data = day04.process_input_file()
    solution = day04.solve_part2(input_data)
    assert solution == 208