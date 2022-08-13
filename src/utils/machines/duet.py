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
    SUB = auto()    # subtract (from register)
    JNZ = auto()    # jump if not zero

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
        regex_sub = re.compile(r"^sub ([a-z]) ([a-z]|-?\d+)$")
        regex_jnz = re.compile(r"^jnz ([a-z]|-?\d+) ([a-z]|-?\d+)$")
        instructions = []
        for line in raw_input.splitlines():
            if len(line := line.strip()) == 0:
                continue
            if match_snd := regex_snd.match(line):
                instructions.append((Instruction.SND, match_snd.group(1)))
            elif match_set := regex_set.match(line):
                instructions.append(
                    (Instruction.SET, match_set.group(1), match_set.group(2)))
            elif match_add := regex_add.match(line):
                instructions.append(
                    (Instruction.ADD, match_add.group(1), match_add.group(2)))
            elif match_mul := regex_mul.match(line):
                instructions.append(
                    (Instruction.MUL, match_mul.group(1), match_mul.group(2)))
            elif match_mod := regex_mod.match(line):
                instructions.append(
                    (Instruction.MOD, match_mod.group(1), match_mod.group(2)))
            elif match_rcv := regex_rcv.match(line):
                instructions.append((Instruction.RCV, match_rcv.group(1)))
            elif match_jgz := regex_jgz.match(line):
                instructions.append(
                    (Instruction.JGZ, match_jgz.group(1), match_jgz.group(2)))
            elif match_sub := regex_sub.match(line):
                instructions.append(
                    (Instruction.SUB, match_sub.group(1), match_sub.group(2)))
            elif match_jnz := regex_jnz.match(line):
                instructions.append(
                    (Instruction.JNZ, match_jnz.group(1), match_jnz.group(2)))
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
        self.awaiting_input = False
        self.halted = False
        self.total_sounds_sent = 0
        self.execution_counts = {instruct: 0 for instruct in Instruction}

    def execute_program(self):
        """
        Executes the program contained within the sound computer.
        """
        if self.halted:
            return
        while 0 <= self.cursor < len(self.instructions):
            self.execution_counts[self.instructions[self.cursor][0]] += 1
            match self.instructions[self.cursor][0]:
                case Instruction.SND:
                    param = self.instructions[self.cursor][1]
                    self.sounds_sent.append(self.try_register_read(param))
                    self.total_sounds_sent += 1
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
                    if not self.duet_mode:
                        check_value = self.try_register_read(param)
                        if check_value != 0:
                            return
                    else:
                        if len(self.sounds_received) == 0:
                            self.awaiting_input = True
                            return
                        self.awaiting_input = False
                        self.registers[param] = self.sounds_received.popleft()
                case Instruction.JGZ:
                    param1 = self.instructions[self.cursor][1]
                    param2 = self.instructions[self.cursor][2]
                    check_value = self.try_register_read(param1)
                    jump_value = self.try_register_read(param2)
                    if check_value > 0:
                        self.cursor += jump_value - 1
                case Instruction.SUB:
                    reg = self.instructions[self.cursor][1]
                    param = self.instructions[self.cursor][2]
                    self.registers[reg] -= self.try_register_read(param)
                case Instruction.JNZ:
                    param1 = self.instructions[self.cursor][1]
                    param2 = self.instructions[self.cursor][2]
                    check_value = self.try_register_read(param1)
                    jump_value = self.try_register_read(param2)
                    if check_value != 0:
                        self.cursor += jump_value - 1
            self.cursor += 1
        self.halted = True

    def get_total_sounds_sent(self):
        """
        Returns the total number of sounds sent by the sound computer.
        """
        return self.total_sounds_sent

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

    def get_sent_sounds(self):
        """
        Gets the sounds sent by the sound computer, and empties the sent buffer
        for the sound computer.
        """
        sounds = self.sounds_sent
        self.sounds_sent = deque([])
        return sounds

    def receive_sounds(self, sounds):
        """
        Adds the sounds to the end of the received queue for the sound computer.
        """
        self.sounds_received.extend(sounds)
        if len(sounds) > 0:
            self.awaiting_input = False

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

    def is_halted(self):
        """
        Checks if the sound computer is halted.
        """
        return self.halted

    def is_awaiting_input(self):
        """
        Checks if the sound computer is awaiting input.
        """
        return self.awaiting_input

    def get_execution_count_mul(self):
        """
        Returns the number of times the SoundComputer has executed the "mul"
        instruction.
        """
        return self.execution_counts[Instruction.MUL]
