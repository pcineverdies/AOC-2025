from typing import Any
from .utils.day import Day
from .utils import aoc

def find_largest(ll: list[int], size: int) -> int:
    result, search_left = 0, 0
    for i in range(size):
        max_index, max_value = max(enumerate(ll[search_left:len(ll) - size + 1 + i]), key=lambda x: x[1])
        result, search_left = result + (max_value * (10 ** (size - i - 1))), max_index + 1 + search_left

    return result

class Day03(Day):

    def day(self, _input: str) -> Any:
        for line in aoc.yield_line(_input):
            line_int = [int(c) for c in line]
            self.ans1 += find_largest(line_int, 2)
            self.ans2 += find_largest(line_int, 12)

        return (self.ans1, self.ans2)

