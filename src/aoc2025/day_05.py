from typing import Any
from .utils.day import Day
from .utils import aoc

def no_overlaps(ranges: list[list[int]]) -> list[list[int]]:
    ranges = sorted(ranges, key=lambda x: x[0])
    result = [ranges[0]]

    for range in ranges[1:]:
        if (range[0] >= result[-1][0] and range[0] <= result[-1][1]) or (range[1] >= result[-1][0] and range[1] <= result[-1][1]):
            result[-1] = [min(range[0], result[-1][0]), max(range[1], result[-1][1])]
        else:
            result.append(range)

    return result

class Day05(Day):

    def day(self, _input: str) -> Any:
        ranges, ingredients = [], []
        for line in aoc.yield_line(_input):

            nums = aoc.str_to_list_unsigned(line)
            if len(nums) == 1:
                ingredients.append(nums[0])
            elif len(nums) == 2:
                ranges.append([nums[0], nums[1]])

        ranges = no_overlaps(ranges)

        self.ans2 = sum([range[1] - range[0] + 1 for range in ranges])
        self.ans1 = sum((ingr>= range[0] and ingr <= range[1] for range in ranges for ingr in ingredients))

        return (self.ans1, self.ans2)

