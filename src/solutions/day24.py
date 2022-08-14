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

def find_strongest_bridge(components):
    """
    Finds the strength of the strongest bridge that can be assembled from the
    given components.
    """
    max_strength = []
    for comp in components:
        if comp[0] == 0:
            remaining_components = list(components)
            remaining_components.remove(comp)
            link = (comp[0], comp[1])
            assembled = [link]
            find_strongest_bridge_recursive(remaining_components, assembled, max_strength)
        elif comp[1] == 0:
            remaining_components = list(components)
            remaining_components.remove(comp)
            link = (comp[1], comp[0])
            assembled = [link]
            find_strongest_bridge_recursive(remaining_components, assembled, max_strength)
    if len(max_strength) == 0:
        return None
    return max_strength[0]

def find_strongest_bridge_recursive(components, assembled, max_strength):
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
            find_strongest_bridge_recursive(remaining_components, new_assembled, max_strength)
        elif comp[1] == assembled[-1][1]:
            remaining_components = list(components)
            new_assembled = list(assembled)
            remaining_components.remove(comp)
            link = (comp[1], comp[0])
            new_assembled.append(link)
            find_strongest_bridge_recursive(remaining_components, new_assembled, max_strength)
    strength = sum(left + right for (left, right) in assembled)
    if len(max_strength) == 0:
        max_strength.append(strength)
    elif strength > max_strength[0]:
        max_strength[0] = strength




def solve_part2(_components):
    """
    Solves AOC 2017 Day 24 Part 2 // ###
    """
    return NotImplemented
