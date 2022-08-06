"""
This module contains the test methods used to test the actual solutions for
each of the solved AOC 2017 problem parts. Test methods utilising pytest
library.
"""

from src.solutions import day01, day02, day03, day04, day05, day06, day07, \
    day08, day09, day10, day11, day12, day13, day14


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


def test_day05_part1():
    """
    Solution test method for AOC 2017 Day 5 Part 1.
    """
    input_data = day05.process_input_file()
    solution = day05.solve_part1(input_data)
    assert solution == 358131


def test_day05_part2():
    """
    Solution test method for AOC 2017 Day 5 Part 2.
    """
    input_data = day05.process_input_file()
    solution = day05.solve_part2(input_data)
    assert solution == 25558839


def test_day06_part1():
    """
    Solution test method for AOC 2017 Day 6 Part 1.
    """
    input_data = day06.process_input_file()
    solution = day06.solve_part1(input_data)
    assert solution == 7864


def test_day06_part2():
    """
    Solution test method for AOC 2017 Day 6 Part 2.
    """
    input_data = day06.process_input_file()
    solution = day06.solve_part2(input_data)
    assert solution == 1695


def test_day07_part1():
    """
    Solution test method for AOC 2017 Day 7 Part 1.
    """
    input_data = day07.process_input_file()
    solution = day07.solve_part1(input_data)
    assert solution == "hlqnsbe"


def test_day07_part2():
    """
    Solution test method for AOC 2017 Day 7 Part 2.
    """
    input_data = day07.process_input_file()
    solution = day07.solve_part2(input_data)
    assert solution == 1993


def test_day08_part1():
    """
    Solution test method for AOC 2017 Day 8 Part 1.
    """
    input_data = day08.process_input_file()
    solution = day08.solve_part1(input_data)
    assert solution == 4902


def test_day08_part2():
    """
    Solution test method for AOC 2017 Day 8 Part 2.
    """
    input_data = day08.process_input_file()
    solution = day08.solve_part2(input_data)
    assert solution == 7037


def test_day09_part1():
    """
    Solution test method for AOC 2017 Day 9 Part 1.
    """
    input_data = day09.process_input_file()
    solution = day09.solve_part1(input_data)
    assert solution == 16869


def test_day09_part2():
    """
    Solution test method for AOC 2017 Day 9 Part 2.
    """
    input_data = day09.process_input_file()
    solution = day09.solve_part2(input_data)
    assert solution == 7284


def test_day10_part1():
    """
    Solution test method for AOC 2017 Day 10 Part 1.
    """
    input_data = day10.process_input_file()
    solution = day10.solve_part1(input_data)
    assert solution == 38628


def test_day10_part2():
    """
    Solution test method for AOC 2017 Day 10 Part 2.
    """
    input_data = day10.process_input_file()
    solution = day10.solve_part2(input_data)
    assert solution == "e1462100a34221a7f0906da15c1c979a"


def test_day11_part1():
    """
    Solution test method for AOC 2017 Day 11 Part 1.
    """
    input_data = day11.process_input_file()
    solution = day11.solve_part1(input_data)
    assert solution == 877


def test_day11_part2():
    """
    Solution test method for AOC 2017 Day 11 Part 2.
    """
    input_data = day11.process_input_file()
    solution = day11.solve_part2(input_data)
    assert solution == 1622


def test_day12_part1():
    """
    Solution test method for AOC 2017 Day 12 Part 1.
    """
    input_data = day12.process_input_file()
    solution = day12.solve_part1(input_data)
    assert solution == 288


def test_day12_part2():
    """
    Solution test method for AOC 2017 Day 12 Part 2.
    """
    input_data = day12.process_input_file()
    solution = day12.solve_part2(input_data)
    assert solution == 211


def test_day13_part1():
    """
    Solution test method for AOC 2017 Day 13 Part 1.
    """
    input_data = day13.process_input_file()
    solution = day13.solve_part1(input_data)
    assert solution == 2160


def test_day13_part2():
    """
    Solution test method for AOC 2017 Day 13 Part 2.
    """
    input_data = day13.process_input_file()
    solution = day13.solve_part2(input_data)
    assert solution == 3907470


def test_day14_part1():
    """
    Solution test method for AOC 2017 Day 14 Part 1.
    """
    input_data = day14.process_input_file()
    solution = day14.solve_part1(input_data)
    assert solution == 8190


def test_day14_part2():
    """
    Solution test method for AOC 2017 Day 14 Part 1.
    """
    input_data = day14.process_input_file()
    solution = day14.solve_part2(input_data)
    assert solution == 1134
