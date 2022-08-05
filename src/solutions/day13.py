"""
Solutions for AOC 2017 Day 13.
"""


def process_input_file(filepath="./input/day13.txt"):
    """
    Processes the AOC 2017 Day 13 input file into the format required by the
    solver functions. Returned value is dict with layer depth mapped to range.
    """
    firewall_layers = {}
    with open(filepath, encoding="utf-8") as file:
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            # Line consists of firewall layer depth mapped to layer range
            layer_data = [int(value) for value in line.split(": ")]
            firewall_layers[layer_data[0]] = layer_data[1]
    return firewall_layers


def solve_part1(firewall_layers):
    """
    Solves AOC 2017 Day 13 Part 1 // Determines the severity score for the whole
    trip of the packet through the firewall described by the given layers.
    """
    # Scanner at top of a layer if its at start of cycle in a layer
    return sum(ldepth * lrange for (ldepth, lrange) in firewall_layers.items()
               if ldepth % (2 * (lrange - 1)) == 0)


def solve_part2(firewall_layers):
    """
    Solves AOC 2017 Day 13 Part 2 // Determines the fewest number of picoseconds
    that the packet needs to be delayed to pass through the firewall without
    being caught.
    """
    delta_ps = 0
    while True:
        caught = False
        for (ldepth, lrange) in firewall_layers.items():
            cycle = 2 * (lrange - 1)
            # Packet reaches the layer at time: ldepth + delta_ps (in ps)
            if (ldepth + delta_ps) % cycle == 0:
                caught = True
                break
        if not caught:
            break
        delta_ps += 1
    return delta_ps
