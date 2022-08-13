"""
This module contains the test methods used to test the actual solutions for
each of the solved AOC 2017 problem parts. Test methods utilising pytest
library.
"""

from src.solutions import day01, day02, day03, day04, day05, day06, day07, \
    day08, day09, day10, day11, day12, day13, day14, day15, day16, day17, \
    day18, day19, day20, day21, day22, day23


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


def test_day15_part1():
    """
    Solution test method for AOC 2017 Day 15 Part 1.
    """
    input_data = day15.process_input_file()
    solution = day15.solve_part1(input_data)
    assert solution == 594


def test_day15_part2():
    """
    Solution test method for AOC 2017 Day 15 Part 2.
    """
    input_data = day15.process_input_file()
    solution = day15.solve_part2(input_data)
    assert solution == 328


def test_day16_part1():
    """
    Solution test method for AOC 2017 Day 16 Part 1.
    """
    input_data = day16.process_input_file()
    solution = day16.solve_part1(input_data)
    assert solution == "pkgnhomelfdibjac"


def test_day16_part2():
    """
    Solution test method for AOC 2017 Day 16 Part 2.
    """
    input_data = day16.process_input_file()
    solution = day16.solve_part2(input_data)
    assert solution == "pogbjfihclkemadn"


def test_day17_part1():
    """
    Solution test method for AOC 2017 Day 17 Part 1.
    """
    input_data = day17.process_input_file()
    solution = day17.solve_part1(input_data)
    assert solution == 1642


def test_day17_part2():
    """
    Solution test method for AOC 2017 Day 17 Part 2.
    """
    input_data = day17.process_input_file()
    solution = day17.solve_part2(input_data)
    assert solution == 33601318


def test_day18_part1():
    """
    Solution test method for AOC 2017 Day 18 Part 1.
    """
    input_data = day18.process_input_file()
    solution = day18.solve_part1(input_data)
    assert solution == 3188


def test_day18_part2():
    """
    Solution test method for AOC 2017 Day 18 Part 2.
    """
    input_data = day18.process_input_file()
    solution = day18.solve_part2(input_data)
    assert solution == 7112


def test_day19_part1():
    """
    Solution test method for AOC 2017 Day 19 Part 1.
    """
    input_data = day19.process_input_file()
    solution = day19.solve_part1(input_data)
    assert solution == "QPRYCIOLU"


def test_day19_part2():
    """
    Solution test method for AOC 2017 Day 19 Part 2.
    """
    input_data = day19.process_input_file()
    solution = day19.solve_part2(input_data)
    assert solution == 16162


def test_day20_part1():
    """
    Solution test method for AOC 2017 Day 20 Part 1.
    """
    input_data = day20.process_input_file()
    solution = day20.solve_part1(input_data)
    assert solution == 376


def test_day20_part2():
    """
    Solution test method for AOC 2017 Day 20 Part 2.
    """
    input_data = day20.process_input_file()
    solution = day20.solve_part2(input_data)
    assert solution == 574


def test_day21_part1():
    """
    Solution test method for AOC 2017 Day 21 Part 1.
    """
    input_data = day21.process_input_file()
    solution = day21.solve_part1(input_data)
    assert solution == 203


def test_day21_part2():
    """
    Solution test method for AOC 2017 Day 21 Part 2.
    """
    input_data = day21.process_input_file()
    solution = day21.solve_part2(input_data)
    assert solution == 3342470


def test_day22_part1():
    """
    Solution test method for AOC 2017 Day 22 Part 1.
    """
    input_data = day22.process_input_file()
    solution = day22.solve_part1(input_data)
    assert solution == 5570


def test_day22_part2():
    """
    Solution test method for AOC 2017 Day 22 Part 2.
    """
    input_data = day22.process_input_file()
    solution = day22.solve_part2(input_data)
    assert solution == 2512022


def test_day23_part1():
    """
    Solution test method for AOC 2017 Day 23 Part 1.
    """
    input_data = day23.process_input_file()
    solution = day23.solve_part1(input_data)
    assert solution == 6241
