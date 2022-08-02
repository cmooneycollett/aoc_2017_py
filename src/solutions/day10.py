"""
Solutions for AOC 2017 Day 10.
"""


def process_input_file(filepath="./input/day10.txt"):
    """
    Processes the AOC 2017 Day 10 input file into the format required by the
    solver functions. Returned value is string of comma-separated values given
    in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        return file.read().strip()


def solve_part1(input_string):
    """
    Solves AOC 2017 Day 10 Part 1 // Returns the product of first two numbers in
    list, initialised with values 0 to 255 in sequence, after applying the knot
    hash algorithm for the given number of lengths.
    """
    lengths = [int(num) for num in input_string.split(",")]
    (strand, _, _) = apply_knot_hash(list(range(256)), lengths)
    return strand[0] * strand[1]


def solve_part2(_input_string):
    """
    Solves AOC 2017 Day 10 Part 2 // ###
    """
    return NotImplemented


def apply_knot_hash(start_strand, lengths, start_cursor=0, start_skip=0):
    """
    Applies a single iteration of the knot hash to the given strand using the
    given length values. Returns the resulting strand after single knot hash
    round, the final cursor value and the final skip value.
    """
    strand = list(start_strand)
    cursor = start_cursor
    skip = start_skip
    for length in lengths:
        # Reverse target segment of list of current length from cursor
        segment = []
        for delta in range(length):
            index = (cursor + delta) % len(strand)
            segment.append(strand[index])
        segment.reverse()
        for delta in range(length):
            index = (cursor + delta) % len(strand)
            strand[index] = segment[delta]
        # Update cursor location and increment skip value
        cursor += length + skip
        skip += 1
    return (strand, cursor, skip)
