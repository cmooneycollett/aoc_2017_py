"""
This module contains the classes required to model the sound computer used in
the AOC 2017 Day 18 problem.
"""

from collections import deque
from enum import Enum, auto, unique
import re
import string


@unique
class Instruction(Enum):
    """
    Represents the different instructions that can be executed by a sound
    computer.
    """
    SND = auto()    # sound / send
    SET = auto()    # set (register)
    ADD = auto()    # add (to register)
    MUL = auto()    # muliply (register)
    MOD = auto()    # modulo
    RCV = auto()    # recover / receive
    JGZ = auto()    # jump if greater than zero

    @classmethod
    def parse_raw_input(cls, raw_input):
        """
        Parses raw input to generate list of instructions. Returns list of
        tuples containing instructions and their parameters.
        """
        regex_snd = re.compile(r"^snd ([a-z]|-?\d+)$")
        regex_set = re.compile(r"^set ([a-z]) ([a-z]|-?\d+)$")
        regex_add = re.compile(r"^add ([a-z]) ([a-z]|-?\d+)$")
        regex_mul = re.compile(r"^mul ([a-z]) ([a-z]|-?\d+)$")
        regex_mod = re.compile(r"^mod ([a-z]) ([a-z]|-?\d+)$")
        regex_rcv = re.compile(r"^rcv ([a-z]|-?\d+)$")
        regex_jgz = re.compile(r"^jgz ([a-z]|-?\d+) ([a-z]|-?\d+)$")
        instructions = []
        for line in raw_input.splitlines():
            if len(line := line.strip()) == 0:
                continue
            if match_snd := regex_snd.match(line):
                instructions.append((Instruction.SND, match_snd.group(1)))
            elif match_set := regex_set.match(line):
                instructions.append((Instruction.SET, match_set.group(1), match_set.group(2)))
            elif match_add := regex_add.match(line):
                instructions.append((Instruction.ADD, match_add.group(1), match_add.group(2)))
            elif match_mul := regex_mul.match(line):
                instructions.append((Instruction.MUL, match_mul.group(1), match_mul.group(2)))
            elif match_mod := regex_mod.match(line):
                instructions.append((Instruction.MOD, match_mod.group(1), match_mod.group(2)))
            elif match_rcv := regex_rcv.match(line):
                instructions.append((Instruction.RCV, match_rcv.group(1)))
            elif match_jgz := regex_jgz.match(line):
                instructions.append((Instruction.JGZ, match_jgz.group(1), match_jgz.group(2)))
        return instructions


class SoundComputer:
    """
    Represents a sound computer that can be operated in either single-mode or
    duet-mode.
    """

    def __init__(self, raw_input, duet_mode=False):
        self.instructions = Instruction.parse_raw_input(raw_input)
        self.registers = {char: 0 for char in string.ascii_lowercase}
        self.duet_mode = duet_mode
        self.cursor = 0
        self.sounds_sent = deque([])
        self.sounds_received = deque([])
        self.is_awaiting_input = False
        self.is_halted = False

    def execute_program(self):
        """
        Executes the program contained within the sound computer.
        """
        while 0 <= self.cursor < len(self.instructions):
            match self.instructions[self.cursor][0]:
                case Instruction.SND:
                    param = self.instructions[self.cursor][1]
                    self.sounds_sent.append(self.try_register_read(param))
                case Instruction.SET:
                    reg = self.instructions[self.cursor][1]
                    param = self.instructions[self.cursor][2]
                    value = self.try_register_read(param)
                    self.registers[reg] = value
                case Instruction.ADD:
                    reg = self.instructions[self.cursor][1]
                    param = self.instructions[self.cursor][2]
                    self.registers[reg] += self.try_register_read(param)
                case Instruction.MUL:
                    param1 = self.instructions[self.cursor][1]
                    param2 = self.instructions[self.cursor][2]
                    self.registers[param1] *= self.try_register_read(param2)
                case Instruction.MOD:
                    param1 = self.instructions[self.cursor][1]
                    param2 = self.instructions[self.cursor][2]
                    self.registers[param1] %= self.try_register_read(param2)
                case Instruction.RCV:
                    param = self.instructions[self.cursor][1]
                    check_value = self.try_register_read(param)
                    if check_value != 0:
                        if not self.duet_mode:
                            return self.sounds_sent[-1]
                case Instruction.JGZ:
                    param1 = self.instructions[self.cursor][1]
                    param2 = self.instructions[self.cursor][2]
                    check_value = self.try_register_read(param1)
                    jump_value = self.try_register_read(param2)
                    if check_value > 0:
                        self.cursor += jump_value - 1
            self.cursor += 1
        self.is_halted = True

    def try_register_read(self, param):
        """
        Trys to read the param from the register, otherwise converts it to
        integer value.
        """
        if param in self.registers:
            return self.registers[param]
        return int(param)

    def set_register(self, register, value):
        """
        Sets the specified register to the given value.
        """
        self.registers[register] = value

    def get_last_played_sound(self):
        """
        Gets the last sound played by the sound computer.
        """
        if len(self.sounds_sent) == 0:
            return None
        return self.sounds_sent[-1]

    def set_duet_mode(self, duet_mode):
        """
        Sets the mode of the sound computer to be duet-mode or single-mode.
        """
        self.duet_mode = duet_mode
