"""
Solutions for AOC 2017 Day 21 - "Fractal Art".
"""

import numpy

def process_input_file(filepath="./input/day21.txt"):
    """
    Processes the AOC 2017 Day 21 input file into the format required by the
    solver functions. Returns dict with the enhancement rules given in the input
    file.
    """
    with open(filepath, encoding="utf-8") as file:
        rules = {}
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            line = line.replace("/", "")
            groups = line.split(" => ")
            key = groups[0]
            value = groups[1]
            rules[key] = value
        return rules


def solve_part1(rules):
    """
    Solves AOC 2017 Day 21 Part 1 // Determines how many pixels stay on after
    applying five iterations of the enhancement rules.
    """
    artgrid = generate_art(rules, 5)
    return (artgrid == b"#").sum()


def solve_part2(rules):
    """
    Solves AOC 2017 Day 21 Part 2 // Determines how many pixels stay on after
    applying 18 iterations of the enhancement rules.
    """
    artgrid = generate_art(rules, 18)
    return (artgrid == b"#").sum()

def generate_art(rules, iterations):
    """
    Generates the art array by applying the specified number of iterations of
    the rules to the starting pattern (3x3): ".#./..#/###"
    """
    artgrid = numpy.array([[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]], dtype="S1")
    for _ in range(iterations):
        if artgrid.shape[0] % 2 == 0:
            new_width = (artgrid.shape[0] // 2) * 3
            new_artgrid = numpy.empty((new_width, new_width), dtype="S1")
            for row in range(0, artgrid.shape[0], 2):
                for col in range(0, artgrid.shape[0], 2):
                    # Create the window grid
                    windowgrid = numpy.empty((2, 2), dtype="S1")
                    for delta_y in range(2):
                        for delta_x in range(2):
                            windowgrid[delta_y][delta_x] = artgrid[row + delta_y][col + delta_x]
                    # For each rotation, check if a rule is matched
                    flip_rules = [[], [numpy.fliplr], [numpy.fliplr, numpy.flipud], [numpy.fliplr]]
                    match_found = False
                    for _ in range(4):
                        windowgrid = numpy.rot90(windowgrid)
                        for position_rules in flip_rules:
                            for func in position_rules:
                                windowgrid = func(windowgrid)
                            key = ""
                            for delta_y in range(2):
                                for delta_x in range(2):
                                    key += windowgrid[delta_y][delta_x].decode("utf-8")
                            if key in rules:
                                value = rules[key]
                                for delta_y in range(3):
                                    for delta_x in range(3):
                                        value_index = delta_y * 3 + delta_x
                                        new_artgrid[row // 2 * 3 + delta_y][col // 2 * 3 + delta_x] = value[value_index]
                                match_found = True
                                break
                        if match_found:
                            break
                        windowgrid = numpy.fliplr(windowgrid)
                        windowgrid = numpy.flipud(windowgrid)
            artgrid = new_artgrid
        elif artgrid.shape[0] % 3 == 0:
            new_width = (artgrid.shape[0] // 3) * 4
            new_artgrid = numpy.empty((new_width, new_width), dtype="S1")
            for row in range(0, artgrid.shape[0], 3):
                for col in range(0, artgrid.shape[0], 3):
                    # Create the window grid
                    windowgrid = numpy.empty((3, 3), dtype="S1")
                    for delta_y in range(3):
                        for delta_x in range(3):
                            windowgrid[delta_y][delta_x] = artgrid[row + delta_y][col + delta_x]
                    # For each rotation, check if a rule is matched
                    flip_rules = [[], [numpy.fliplr], [numpy.fliplr, numpy.flipud], [numpy.fliplr]]
                    match_found = False
                    for _ in range(4):
                        windowgrid = numpy.rot90(windowgrid)
                        for position_rules in flip_rules:
                            for func in position_rules:
                                windowgrid = func(windowgrid)
                            key = ""
                            for delta_y in range(3):
                                for delta_x in range(3):
                                    key += windowgrid[delta_y][delta_x].decode("utf-8")
                            if key in rules:
                                value = rules[key]
                                for delta_y in range(4):
                                    for delta_x in range(4):
                                        value_index = delta_y * 4 + delta_x
                                        new_artgrid[row // 3 * 4 + delta_y][col // 3 * 4 + delta_x] = value[value_index]
                                match_found = True
                                break
                        if match_found:
                            break
                        windowgrid = numpy.fliplr(windowgrid)
                        windowgrid = numpy.flipud(windowgrid)
            artgrid = new_artgrid
    return artgrid
