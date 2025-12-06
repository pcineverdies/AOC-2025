from typing import Any
from .utils.day import Day
from .utils import aoc

def operation_from_matrix(matrix: list[list[str]], is_mul: bool) -> int:
    result = 1 if is_mul else 0
    for row in matrix:
        number = int("".join([c for c in row if c != " "]))
        result = result * number if is_mul else result + number
    return result

class Day06(Day):

    def day(self, _input: str) -> Any:
        last_index, idx, ops, matrix_input = 0, 0, [], []
        for line in aoc.yield_line(_input):
            if "+" not in line:
                matrix_input.append(aoc.str_to_list_char(line))
            else:
                ops = [ch for ch in line if not ch.isspace()]

        for j in range(len(matrix_input[0])):
            if not all(matrix_input[i][j] == " " for i in range(len(matrix_input))):
                continue
            small_matrix = [row[last_index:j] for row in matrix_input]
            self.ans1 += operation_from_matrix(small_matrix, ops[idx] == "*")
            self.ans2 += operation_from_matrix(list(map(list, zip(*small_matrix))), ops[idx] == "*")
            last_index, idx = j + 1, idx + 1

        return (self.ans1, self.ans2)

