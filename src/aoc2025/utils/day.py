from typing import Any, Optional

class Day:

    def __init__(self,
                 day_number: int,
                 test_input: Optional[list[str]],
                 input: Optional[str]) -> None:

        self.day_number = day_number
        self.test_input = test_input
        self.input = input

    def part_1(self, _input: str) -> Any:
        pass

    def part_2(self, _input: str) -> Any:
        pass

    def run(self, part: int) -> Any:

        if part == 1:
            if self.test_input:
                for index, test in enumerate(self.test_input):
                    print(f"Day {self.day_number} - Part 1 - Test {index + 1}: {self.part_1(test)}")
            if self.input:
                print(f"Day {self.day_number} - Part 1 - Result: {self.part_1(self.input)}")
        else:
            if self.test_input:
                for index, test in enumerate(self.test_input):
                    print(f"Day {self.day_number} - Part 2 - Test {index + 1}: {self.part_2(test)}")

            if self.input:
                print(f"Day {self.day_number} - Part 2 - Result: {self.part_2(self.input)}")
