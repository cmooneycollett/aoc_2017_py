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


def solve_part2(input_string):
    """
    Solves AOC 2017 Day 10 Part 2 // Determines the knot hash of the input
    string, including input processing (length sequence suffix append), 64
    rounds of knot hash algorithm and output processing (dense hash calculation
    and conversion to hexadecimal string).
    """
    # Input processing
    lengths = [ord(char) for char in input_string]
    lengths.extend([17, 31, 73, 47, 23])
    # Apply 64 rounds of knot hash algorithm
    strand = list(range(256))
    cursor = 0
    skip = 0
    for _ in range(64):
        (strand, cursor, skip) = apply_knot_hash(strand, lengths, cursor, skip)
    # Convert to dense hash
    dense_hash = []
    for block in range(16):
        block_start = block * 16
        xor_result = strand[block_start]
        for delta in range(1, 16):
            xor_result ^= strand[block_start + delta]
        dense_hash.append(xor_result)
    # Convert dense hash to hexidecimal representation
    hex_digest = [str(hex(block))[2:] for block in dense_hash]
    return "".join(hex_digest)


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
        cursor = (cursor + length + skip) % len(strand)
        skip += 1
    return (strand, cursor, skip)
