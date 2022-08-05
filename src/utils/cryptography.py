"""
This module contains any code relating to cryptography, including "toy" hash
algorithms.
"""


def calculate_knot_hash(input_string):
    """
    Determines the knot hash of the input string, including input processing
    (length sequence suffix append), 64 rounds of knot hash algorithm and output
    processing (dense hash calculation and conversion to hexadecimal string).
    """
    # Input processing
    lengths = [ord(char) for char in input_string]
    lengths.extend([17, 31, 73, 47, 23])
    # Apply 64 rounds of knot hash algorithm
    strand = list(range(256))
    cursor = 0
    skip = 0
    for _ in range(64):
        (strand, cursor, skip) = calculate_sparse_hash(strand, lengths, cursor,
                                                       skip)
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


def calculate_sparse_hash(start_strand, lengths, start_cursor=0, start_skip=0):
    """
    Finds the sparse hash of the given strand. Returns the sparse hash of the
    starting strand, the final cursor value and the final skip value.
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
