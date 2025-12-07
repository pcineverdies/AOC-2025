from typing import Any
from ..utils.day import Day
from ..utils import aoc

def can_be_removed(matrix: aoc.Matrix) -> list[aoc.Coordinate]:
    result = []
    for c in matrix.yield_coordinate():
        if matrix.get_coordinate(c) != "@":
            continue

        counter = (matrix.get_coordinate(c + aoc.D, ".") == "@") + (matrix.get_coordinate(c + aoc.UL, ".") == "@") + \
                  (matrix.get_coordinate(c + aoc.U, ".") == "@") + (matrix.get_coordinate(c + aoc.DL, ".") == "@") + \
                  (matrix.get_coordinate(c + aoc.R, ".") == "@") + (matrix.get_coordinate(c + aoc.UR, ".") == "@") + \
                  (matrix.get_coordinate(c + aoc.L, ".") == "@") + (matrix.get_coordinate(c + aoc.DR, ".") == "@")

        if counter < 4:
            result.append(c)

    return result

class Day04(Day):

    def day(self, _input: str) -> Any:
        matrix = aoc.matrix_from_input(_input)

        for iteration in range(100000):
            to_remove = can_be_removed(matrix)
            if len(to_remove) == 0:
                break
            self.ans1 += len(to_remove) if iteration == 0 else 0
            self.ans2 += len(to_remove)
            [matrix.set_coordinate(c, ".") for c in to_remove]


        return (self.ans1, self.ans2)

