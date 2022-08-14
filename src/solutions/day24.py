"""
Solutions for AOC 2017 Day 24 - "Electromagnetic Moat".
"""


def process_input_file(filepath="./input/day24.txt"):
    """
    Processes the AOC 2017 Day 24 input file into the format required by the
    solver functions. Returns a list of tuples specifying the electromagnetic
    connectors given in the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        components = []
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            sides = line.split("/")
            components.append((int(sides[0]), int(sides[1])))
    return components


def solve_part1(components):
    """
    Solves AOC 2017 Day 24 Part 1 // Determines the strength of the bridge with
    the greatest strength that can be assembled from the given components.
    """
    return find_strongest_bridge(components)


def solve_part2(components):
    """
    Solves AOC 2017 Day 24 Part 2 // Determines the strength of the longest
    bridge that can be assembled from the given components, with the highest
    strength taken if there are multiple bridges with the longest length.
    """
    return find_strongest_bridge(components, for_longest_bridge=True)


def find_strongest_bridge(components, for_longest_bridge=False):
    """
    Finds the strength of the strongest bridge that can be assembled from the
    given components.
    """
    bridge_strength_length = []
    for comp in components:
        if comp[0] == 0:
            remaining_components = list(components)
            remaining_components.remove(comp)
            link = (comp[0], comp[1])
            assembled = [link]
            find_strongest_bridge_recursive(
                remaining_components, assembled, bridge_strength_length, for_longest_bridge)
        elif comp[1] == 0:
            remaining_components = list(components)
            remaining_components.remove(comp)
            link = (comp[1], comp[0])
            assembled = [link]
            find_strongest_bridge_recursive(
                remaining_components, assembled, bridge_strength_length, for_longest_bridge)
    if len(bridge_strength_length) == 0:
        return None
    return bridge_strength_length[0][0]


def find_strongest_bridge_recursive(components, assembled, bridge_strength_length,
                                    for_longest_bridge):
    """
    Extends the currently assembled components if possible. If the assembly
    cannot be extended further, calculates its strength and updates max_strength
    if required.
    """
    for comp in components:
        if comp[0] == assembled[-1][1]:
            remaining_components = list(components)
            new_assembled = list(assembled)
            remaining_components.remove(comp)
            link = (comp[0], comp[1])
            new_assembled.append(link)
            find_strongest_bridge_recursive(
                remaining_components, new_assembled, bridge_strength_length, for_longest_bridge)
        elif comp[1] == assembled[-1][1]:
            remaining_components = list(components)
            new_assembled = list(assembled)
            remaining_components.remove(comp)
            link = (comp[1], comp[0])
            new_assembled.append(link)
            find_strongest_bridge_recursive(
                remaining_components, new_assembled, bridge_strength_length, for_longest_bridge)
    # Calculate bridge strength and check for length and strength
    strength = sum(left + right for (left, right) in assembled)
    if len(bridge_strength_length) == 0:
        bridge_strength_length.append((strength, len(assembled)))
    elif for_longest_bridge:
        if len(assembled) > bridge_strength_length[0][1]:
            bridge_strength_length[0] = (strength, len(assembled))
        elif len(assembled) == bridge_strength_length[0][1] and \
                strength > bridge_strength_length[0][0]:
            bridge_strength_length[0] = (strength, len(assembled))
    else:
        if strength > bridge_strength_length[0][0]:
            bridge_strength_length[0] = (strength, len(assembled))
