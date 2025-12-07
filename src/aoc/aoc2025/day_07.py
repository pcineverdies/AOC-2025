# type: ignore
from functools import lru_cache
from typing import Any
from ..utils.day import Day
from ..utils import aoc

@lru_cache(maxsize=10000)
def find_timelines(c: aoc.Coordinate, use_visited) -> int:
    next = c + aoc.D

    if use_visited:
        find_timelines.cache_clear()
        if next in find_timelines.visited:
            return 0
        find_timelines.visited.add(next)

    if find_timelines.grid.get_coordinate(next, "") == "^":
        return find_timelines(next + aoc.L, use_visited) + find_timelines(next + aoc.R, use_visited) + (1 if use_visited else 0)
    return find_timelines(next, use_visited) if next.i < find_timelines.grid.rows else 0 if use_visited else 1

find_timelines.visited, find_timelines.grid = set(), aoc.Matrix(1, 1, 0)

class Day07(Day):

    def day(self, _input: str) -> Any:
        find_timelines.grid = aoc.matrix_from_input(_input)
        return (find_timelines(find_timelines.grid.find_value("S"), True), find_timelines(find_timelines.grid.find_value("S"), False))
