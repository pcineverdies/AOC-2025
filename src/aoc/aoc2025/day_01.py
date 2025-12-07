from typing import Any
from ..utils.day import Day
from ..utils import aoc

class Day01(Day):

    def day(self, _input: str) -> Any:
        counter = 50
        for line in aoc.yield_line(_input):

            for _ in range(aoc.str_to_list_int(line)[0]):
                counter = (counter + (-1 if line[0] == 'L' else 1)) % 100
                self.ans2 += (counter == 0)
            self.ans1 += (counter == 0)

        return (self.ans1, self.ans2)

