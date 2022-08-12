"""
Solutions for AOC 2017 Day 20 - "Particle Swarm".
"""

from collections import deque
from enum import Enum, auto, unique
import re


@unique
class DistanceGrade(Enum):
    """
    Represents the different grades that a particle can be assigned based on the
    rate at which its distance from the origin (0,0,0) is changing.
    """
    INCREASING_HIGHER = auto()
    INCREASING_SAME = auto()
    INCREASING_LOWER = auto()
    SAME = auto()
    DECREASING_LOWER = auto()
    DECREASING_SAME = auto()
    DECREASING_HIGHER = auto()

    @classmethod
    def determine_grade(cls, distances):
        """
        Determines the distance grade based on the distances given. Returns None
        of length of distances object is less than 3.
        """
        if len(distances) < 4:
            return None
        # Calculate changes in distance - velocity deltas
        vel_delta0 = distances[1] - distances[0]
        vel_delta1 = distances[2] - distances[1]
        vel_delta2 = distances[3] - distances[2]
        # Calculate velocity deltas
        acc_delta0 = vel_delta1 - vel_delta0
        acc_delta1 = vel_delta2 - vel_delta1
        # Staying at same distance from origin
        if acc_delta1 == 0:
            return DistanceGrade.SAME
        # Increasing in distance from origin
        if acc_delta1 > 0:
            if acc_delta1 > acc_delta0:
                return DistanceGrade.INCREASING_HIGHER
            if acc_delta1 == acc_delta0:
                return DistanceGrade.INCREASING_SAME
            if acc_delta1 < acc_delta0:
                return DistanceGrade.INCREASING_LOWER
        # Decreasing in distance from origin
        if acc_delta1 < 0:  # acc_delta1 < 0
            if acc_delta1 > acc_delta0:
                return DistanceGrade.DECREASING_LOWER
            if acc_delta1 == acc_delta0:
                return DistanceGrade.DECREASING_SAME
            if acc_delta1 < acc_delta0:
                return DistanceGrade.DECREASING_HIGHER
        # Invalid input
        return None


class Particle:
    """
    Represents a point particle in three-dimensional Euclidean space, with
    three-dimensional position, velocity and acceleration with integer values
    """

    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def get_manhattan_distance_origin(self):
        """
        Calculates the Manhattan distance of the particle from the origin
        (0,0,0).
        """
        return sum(abs(val) for val in self.pos)

    def move(self):
        """
        Updates the particle parameters by first changing particle velocity
        based on acceleration, then position based on new velocity.
        """
        # Update velocity
        self.vel = (self.vel[0] + self.acc[0], self.vel[1] + self.acc[1],
                    self.vel[2] + self.acc[2])
        # Update position
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1],
                    self.pos[2] + self.vel[2])

    def check_collision(self, other_pos):
        """
        Checks if the particle's position and the other position are the same.
        """
        return self.pos == other_pos


def process_input_file(filepath="./input/day20.txt"):
    """
    Processes the AOC 2017 Day 20 input file into the format required by the
    solver functions. Returns dict of particle IDs mapped to particles, as
    specified by the input file.
    """
    with open(filepath, encoding="utf-8") as file:
        regex_particle = re.compile(
            r"^p=<(-?\d+),(-?\d+),(-?\d+)>, v=<(-?\d+),(-?\d+),(-?\d+)>, "
            r"a=<(-?\d+),(-?\d+),(-?\d+)>$")
        particles = {}
        count = 0
        for line in file.readlines():
            if len(line := line.strip()) == 0:
                continue
            if match_particle := regex_particle.match(line):
                pos = tuple(int(val) for val in (match_particle.group(i)
                            for i in range(1, 4)))
                vel = tuple(int(val) for val in (match_particle.group(i)
                            for i in range(4, 7)))
                acc = tuple(int(val) for val in (match_particle.group(i)
                            for i in range(7, 10)))
                particles[count] = Particle(pos, vel, acc)
                count += 1
        return particles


def solve_part1(input_particles):
    """
    Solves AOC 2017 Day 20 Part 1 // Determines the ID of the particle that
    stays closest to the origin (0,0,0) in the long-term.
    """
    (particle_id, _) = simulate_particles(input_particles)
    return particle_id


def solve_part2(_input_particles):
    """
    Solves AOC 2017 Day 20 Part 2 // ###
    """
    return NotImplemented


def simulate_particles(input_particles, removed_collided=False):
    """
    Simulates the movement of the given particles. Returns the ID of the
    particle that remains closest to the origin (0,0,0) in the long-term and
    the number of particles remaining once all collisions have been resolved.
    """
    particle_distances = {}
    particles = dict(input_particles)
    # Record initial distance of each particle from origin
    for (code, particle) in particles.items():
        dist = particle.get_manhattan_distance_origin()
        particle_distances[code] = deque([dist])
    while True:
        # Update particle locations
        distance_grades = {}
        for code in particles:
            particles[code].move()
            dist = particles[code].get_manhattan_distance_origin()
            particle_distances[code].append(dist)
            while len(particle_distances[code]) > 4:
                particle_distances[code].popleft()
            if len(particle_distances[code]) == 4:
                distance_grades[code] = DistanceGrade.determine_grade(
                    particle_distances[code])
        # Remove particles that have collided
        if removed_collided:
            ()
        # Check distance grades
        if len(distance_grades) == len(particles):
            count_same = list(distance_grades.values()
                              ).count(DistanceGrade.SAME)
            count_inc_low = list(distance_grades.values()).count(
                DistanceGrade.INCREASING_LOWER)
            count_inc_same = list(distance_grades.values()).count(
                DistanceGrade.INCREASING_SAME)
            count_inc_high = list(distance_grades.values()).count(
                DistanceGrade.INCREASING_HIGHER)
            check_count = count_same + count_inc_same + count_inc_high
            if check_count == len(distance_grades):
                # Find the particle with lowest rate of distance change from origin
                candidates = set()
                if count_same > 0:
                    candidates = set(code for (code, grade) in distance_grades.items()
                                     if grade == DistanceGrade.SAME)
                elif count_inc_low:
                    candidates = set(code for (code, grade) in distance_grades.items()
                                     if grade == DistanceGrade.INCREASING_LOWER)                                  
                elif count_inc_same > 0:
                    candidates = set(code for (code, grade) in distance_grades.items()
                                     if grade == DistanceGrade.INCREASING_SAME)
                else:
                    candidates = set(code for (code, grade) in distance_grades.items()
                                     if grade == DistanceGrade.INCREASING_HIGHER)
                candidate_distances = {code: dist[-1] for (code, dist) in
                                       particle_distances.items() if code in candidates}
                particle_id = min(candidate_distances, key=candidate_distances.get)
                return (particle_id, len(particles))
