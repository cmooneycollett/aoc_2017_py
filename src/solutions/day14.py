"""
Solutions for AOC 2017 Day 14.
"""

from collections import deque
from src.utils.cartography import Location2D
from src.utils.cryptography import calculate_knot_hash


def process_input_file(filepath="./input/day14.txt"):
    """
    Processes the AOC 2017 Day 14 input file into the format required by the
    solver functions. Returned value is the key string given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(key):
    """
    Solves AOC 2017 Day 14 Part 1 // Calculates the number of used squares in
    the 128-by-128 disk grid using the given key string as seed for knot hashes
    for each row.
    """
    used_count = 0
    for row in range(128):
        knot_hash = calculate_knot_hash(f"{key}-{row}")
        for hex_char in knot_hash:
            used_count += bin(int(hex_char, 16))[2:].zfill(4).count("1")
    return used_count


def solve_part2(key):
    """
    Solves AOC 2017 Day 14 Part 2 // Calculates the number of regions in the
    128-by-128 disk grid given the key string.
    """
    # Populate the disk grid - "0" for free space, "1" for used space
    disk_array = []
    for row in range(128):
        disk_row = []
        knot_hash = calculate_knot_hash(f"{key}-{row}")
        for hex_char in knot_hash:
            bits = bin(int(hex_char, 16))[2:].zfill(4)
            disk_row.extend(bits)
        disk_array.append(disk_row)
    # Find regions using BFS method
    visited = set()
    regions = 0
    for row in range(128):
        for col in range(128):
            # Free space is not in a region
            if disk_array[row][col] == "0":
                continue
            # Check for the start of new region
            loc = Location2D(col, row)
            if loc not in visited:
                region_members = find_region_members(disk_array, loc)
                visited.update(region_members)
                regions += 1
    return regions


def find_region_members(disk_array, loc2d):
    """
    Finds the members of the region including the given 2D-point.
    """
    visited = set()
    state_queue = deque([loc2d])
    while len(state_queue) > 0:
        location = state_queue.popleft()
        visited.add(location)
        for next_location in find_adjacent_used_locations(disk_array, location):
            if next_location not in visited:
                state_queue.append(next_location)
    return visited


def find_adjacent_used_locations(disk_array, loc2d):
    """
    Yields the used locations in the disk grid that are adjacent to the given
    2D-point (diagonals not included).
    """
    for delta in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_x = loc2d.loc_x + delta[0]
        new_y = loc2d.loc_y + delta[1]
        # Skip locations that are outside of the disk array
        if new_x < 0 or new_y < 0 or new_x >= 128 or new_y >= 128:
            continue
        # Skip locations that are marked as "free" space
        if disk_array[new_y][new_x] == "0":
            continue
        yield Location2D(new_x, new_y)
