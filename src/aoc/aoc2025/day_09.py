from typing import Any
from ..utils.day import Day
from ..utils import aoc

class Day09(Day):

    def day(self, _input: str) -> Any:
        coordinates = []
        for line in aoc.yield_line(_input):
            numbers = aoc.str_to_list_int(line)
            coordinates.append(aoc.Coordinate(numbers[1], numbers[0]))

        area_list = []
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                c1, c2 = coordinates[i], coordinates[j]
                area = (abs(c1.i - c2.i) + 1) * (abs(c1.j - c2.j) + 1)
                self.ans1 = max(self.ans1, area)
                area_list.append((area, c1, c2))

        for area, c1, c2 in sorted(area_list, key=lambda x: -x[0]):

            xmax, xmin, ymax, ymin = max(c1.i, c2.i), min(c1.i, c2.i), max(c1.j, c2.j), min(c1.j, c2.j)

            valid = True
            for i in range(len(coordinates)):
                ci, cj = coordinates[i], coordinates[(i + 1) % len(coordinates)]

                xcmax, xcmin, ycmax, ycmin = max(ci.i, cj.i), min(ci.i, cj.i), max(ci.j, cj.j), min(ci.j, cj.j)
                if not (xmin >= xcmax or xmax <= xcmin or ymin >= ycmax or ymax <= ycmin):
                    valid = False
                    break

            if valid:
                self.ans2 = area
                break

        return (self.ans1, self.ans2)

