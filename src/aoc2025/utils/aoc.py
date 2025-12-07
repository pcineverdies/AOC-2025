from __future__ import annotations
from typing import Generator, Callable, Any
import re


def yield_line(input: str) -> Generator[str, None, None]:
    for line in input.splitlines():
        yield line


def zip(l1: list[Any], l2: list[Any], f: Callable[[Any, Any], None]) -> None:
    assert(len(l1) == len(l2))
    [f(l1[i], l2[i]) for i in range(len(l1))]


def str_to_list_int(line: str) -> list[int]:
    pattern = r"[+-]?\d+(?:\.\d+)?"
    matches = re.findall(pattern, line)
    return [int(m) for m in matches]

def str_to_list_unsigned(line: str) -> list[int]:
    pattern = r"\d+(?:\.\d+)?"
    matches = re.findall(pattern, line)
    return [int(m) for m in matches]


def str_to_list_char(line: str) -> list[str]:
    return [c for c in line]


class Coordinate:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coordinate):
            return NotImplemented
        return self.i == other.i and self.j == other.j

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def manhattan(self, other: Coordinate) -> int:
        return abs(self.i - other.i) + abs(self.j - other.j)

    def move(self, di: int, dj: int) -> None:
        self.i = self.i + di
        self.j = self.j + dj

    def get_move(self, di: int, dj: int) -> Coordinate:
        return Coordinate(self.i + di, self.j + dj)

    def __add__(self, c: Coordinate) -> Coordinate:
        return Coordinate(self.i + c.i, self.j + c.j)

    def __repr__(self) -> str:
        return f"({self.i}, {self.j})"

    def __hash__(self) -> int:
        return hash((self.i, self.j))

U = Coordinate(-1, 0)
D = Coordinate(1, 0)
L = Coordinate(0, -1)
R = Coordinate(0, 1)
UR = Coordinate(-1, 1)
UL = Coordinate(-1, -1)
DR = Coordinate(1, 1)
DL = Coordinate(1, -1)

class Matrix:

    def __init__(self, rows: int, columns: int, default: Any = 0) -> None:
        self.rows = rows
        self.columns = columns
        self.m: list[list[Any]] = [[default for _i in range(columns)] for _j in range(rows)]

    def get(self, r: int, c: int, default: Any = None) -> Any:
        if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
            if default is not None:
                return default
            raise ValueError(f"index ({r}, {c}) out of index for matrix with size ({self.rows}, {self.columns})")
        return self.m[r][c]

    def get_coordinate(self, c: Coordinate, default: Any = None) -> Any:
        return self.get(c.i, c.j, default)

    def set(self, r: int, c: int, value: Any) -> None:
        if r < 0 or r >= self.rows or c < 0 or c >= self.columns:
            raise ValueError(f"index ({r}, {c}) out of index for matrix with size ({self.rows}, {self.columns})")
        self.m[r][c] = value

    def set_coordinate(self, c: Coordinate, value: Any) -> None:
        self.set(c.i, c.j, value)

    def __repr__(self) -> str:
        result = ""
        for index, line in enumerate(self.m):
            for c in line:
                result += c
            if index != len(self.m) - 1:
                result += "\n"
        return result

    def is_equal_to(self, r: int, c: int, default: Any, value: Any):
        return self.get(r, c, default) == value

    def yield_coordinate(self) -> Generator[Coordinate, None, None]:
        for i in range(self.rows):
            for j in range(self.columns):
                yield Coordinate(i, j)

    def find_value(self, value: Any) -> Coordinate:
        for c in self.yield_coordinate():
            if self.get_coordinate(c) == value:
                return c
        raise ValueError(f"Value {value} not found in matrix")


def matrix_from_input(grid: str) -> Matrix:

    rows, columns = len(grid.splitlines()), len(grid.splitlines()[0])
    m = Matrix(rows, columns)
    for row, line in enumerate(yield_line(grid)):
        for column, c in enumerate(line):
            m.set(row, column, c)

    return m

