import math
from typing import Any
from .utils.day import Day
from .utils import aoc

def is_valid(num: int) -> bool:

    digits = int(math.log10(num)) + 1

    for i in range(1, digits // 2 + 1):

        if digits % i != 0:
            continue

        power = int(10 ** i)
        expected, found_error, num_temp = num % power, False, num // power

        while num_temp:
            expected_temp, num_temp = num_temp % power, num_temp // power
            if expected_temp != expected:
                found_error = True
                break

        if not found_error:
            return False

    return True

def is_valid_half(num: int) -> bool:
    digits = int(math.log10(num)) + 1
    if digits % 2 != 0:
        return True
    power = 10 ** (digits // 2)
    return (num // power) != (num % power)


class Day02(Day):

    def day(self, _input: str) -> Any:
        ids = []
        for line in aoc.yield_line(_input):
            ids += [tuple(map(int, part.split("-"))) for part in line.split(",")]

        for pair in ids:
            for elem in range(pair[0], pair[1] + 1):
                self.ans1 += elem if not is_valid_half(elem) else 0
                self.ans2 += elem if not is_valid(elem) else 0

        return (self.ans1, self.ans2)

