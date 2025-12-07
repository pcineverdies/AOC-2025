from typing import Any
from ..utils.day import Day
from ..utils import aoc

class DayXX(Day):

    def day(self, _input: str) -> Any:
        for line in aoc.yield_line(_input):
            pass

        return (self.ans1, self.ans2)

