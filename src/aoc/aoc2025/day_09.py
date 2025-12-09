from functools import lru_cache
from typing import Any
from ..utils.day import Day
from ..utils import aoc

coordinates_set = set()
coordinates = []

@lru_cache(maxsize=10000000000)
def is_green(coordinate: aoc.Coordinate) -> bool:
    global coordinates_set
    global coordinates
    counter = 0
    n = len(coordinates)

    if coordinate in coordinates_set:
        return True

    px, py = coordinate.j, coordinate.i

    for k in range(n):
        p1, p2 = coordinates[k], coordinates[(k + 1) % n]
        x1, y1, x2, y2 = p1.j, p1.i, p2.j, p2.i
        dx, dy, dxp, dyp = x2 - x1, y2 - y1, px - x1, py - y1

        if dx * dyp - dy * dxp == 0:
            if min(x1, x2) <= px <= max(x1, x2) and min(y1, y2) <= py <= max(y1, y2):
                return True

        if (y1 > py) != (y2 > py) and (px < (x1 + (py - y1) * (x2 - x1) / (y2 - y1))):
            counter += 1

    return (counter % 2) == 1

class Day09(Day):

    def day(self, _input: str) -> Any:
        global coordinates_set
        global coordinates
        coordinates = []
        for line in aoc.yield_line(_input):
            numbers = aoc.str_to_list_int(line)
            coordinates.append(aoc.Coordinate(numbers[1], numbers[0]))

        area_list = []
        coordinates_set = set(coordinates)
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                c1, c2 = coordinates[i], coordinates[j]
                area = (abs(c1.i - c2.i) + 1) * (abs(c1.j - c2.j) + 1)
                self.ans1 = max(self.ans1, area)
                area_list.append((area, c1, c2))

        for area, c1, c2 in sorted(area_list, key=lambda x: -x[0]):
            xmax, xmin, ymax, ymin = max(c1.i, c2.i), min(c1.i, c2.i), max(c1.j, c2.j), min(c1.j, c2.j)
            is_green_okay = True
            for x in range(xmin, xmax + 1):
                is_green_okay = is_green_okay and is_green(aoc.Coordinate(x, ymin))
                if not is_green_okay:
                    break
                is_green_okay = is_green_okay and is_green(aoc.Coordinate(x, ymax))
                if not is_green_okay:
                    break
            for y in range(ymin, ymax + 1):
                if not is_green_okay:
                    break
                is_green_okay = is_green_okay and is_green(aoc.Coordinate(xmin, y))
                if not is_green_okay:
                    break
                is_green_okay = is_green_okay and is_green(aoc.Coordinate(xmax, y))
                if not is_green_okay:
                    break

            if is_green_okay:
                self.ans2 = area
                break

        return (self.ans1, self.ans2)

