"""
This module contains additional test methods used to test AOC 2017 solution
code against example inputs. Test methods utilising pytest library.
"""

from src.solutions import day07, day08, day09, day12, day13, day14, day15, \
    day18


def test_day07_part1_ex01():
    """
    Test method for AOC 2017 Day 7 Part 1 using example input 1.
    """
    input_data = day07.process_input_file("./input/examples/day07_ex01.txt")
    solution = day07.solve_part1(input_data)
    assert solution == "tknk"


def test_day07_part2_ex01():
    """
    Test method for AOC 2017 Day 7 Part 1 using example input 1.
    """
    input_data = day07.process_input_file("./input/examples/day07_ex01.txt")
    solution = day07.solve_part2(input_data)
    assert solution == 60


def test_day08_part1_ex01():
    """
    Test method for AOC 2017 Day 8 Part 1 using example input 1.
    """
    input_data = day08.process_input_file("./input/examples/day08_ex01.txt")
    solution = day08.solve_part1(input_data)
    assert solution == 1


def test_day08_part2_ex01():
    """
    Test method for AOC 2017 Day 8 Part 2 using example input 1.
    """
    input_data = day08.process_input_file("./input/examples/day08_ex01.txt")
    solution = day08.solve_part2(input_data)
    assert solution == 10


def test_day09_part1_ex07():
    """
    Test method for AOC 2017 Day 9 Part 1 using example input 7.
    """
    input_data = day09.process_input_file("./input/examples/day09_ex07.txt")
    solution = day09.solve_part1(input_data)
    assert solution == 9


def test_day09_part2_ex01():
    """
    Test method for AOC 2017 Day 9 Part 2 using example input 1.
    """
    input_data = day09.process_input_file("./input/examples/day09_ex01.txt")
    solution = day09.solve_part2(input_data)
    assert solution == 0


def test_day09_part2_ex08():
    """
    Test method for AOC 2017 Day 9 Part 2 using example input 8.
    """
    input_data = day09.process_input_file("./input/examples/day09_ex08.txt")
    solution = day09.solve_part2(input_data)
    assert solution == 10


def test_day12_part1_ex01():
    """
    Test method for AOC 2017 Day 12 Part 1 using example input 1.
    """
    input_data = day12.process_input_file("./input/examples/day12_ex01.txt")
    solution = day12.solve_part1(input_data)
    assert solution == 6


def test_day12_part2_ex01():
    """
    Test method for AOC 2017 Day 12 Part 2 using example input 1.
    """
    input_data = day12.process_input_file("./input/examples/day12_ex01.txt")
    solution = day12.solve_part2(input_data)
    assert solution == 2


def test_day13_part1_ex01():
    """
    Test method for AOC 2017 Day 13 Part 1 using example input 1.
    """
    input_data = day13.process_input_file("./input/examples/day13_ex01.txt")
    solution = day13.solve_part1(input_data)
    assert solution == 24


def test_day13_part2_ex01():
    """
    Test method for AOC 2017 Day 13 Part 2 using example input 1.
    """
    input_data = day13.process_input_file("./input/examples/day13_ex01.txt")
    solution = day13.solve_part2(input_data)
    assert solution == 10


def test_day14_part1_ex01():
    """
    Test method for AOC 2017 Day 14 Part 1 using example input 1.
    """
    input_data = day14.process_input_file("./input/examples/day14_ex01.txt")
    solution = day14.solve_part1(input_data)
    assert solution == 8108


def test_day14_part2_ex01():
    """
    Test method for AOC 2017 Day 14 Part 2 using example input 1.
    """
    input_data = day14.process_input_file("./input/examples/day14_ex01.txt")
    solution = day14.solve_part2(input_data)
    assert solution == 1242


def test_day15_part1_ex01():
    """
    Test method for AOC 2017 Day 15 Part 1 using example input 1.
    """
    input_data = day15.process_input_file("./input/examples/day15_ex01.txt")
    solution = day15.solve_part1(input_data)
    assert solution == 588


def test_day15_part2_ex01():
    """
    Test method for AOC 2017 Day 15 Part 2 using example input 1.
    """
    input_data = day15.process_input_file("./input/examples/day15_ex01.txt")
    solution = day15.solve_part2(input_data)
    assert solution == 309


def test_day18_part1_ex01():
    """
    Test method for AOC 2017 Day 18 Part 1 using example input 1.
    """
    input_data = day18.process_input_file("./input/examples/day18_ex01.txt")
    solution = day18.solve_part1(input_data)
    assert solution == 4


def test_day18_part2_ex02():
    """
    Test method for AOC 2017 Day 18 Part 2 using example input 2.
    """
    input_data = day18.process_input_file("./input/examples/day18_ex02.txt")
    solution = day18.solve_part2(input_data)
    assert solution == 3
