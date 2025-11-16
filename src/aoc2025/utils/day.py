from typing import Any, Optional

class Day:

    def __init__(self,
                 day_number: int,
                 test_input: Optional[list[str]],
                 input: Optional[str]) -> None:

        self.day_number = day_number
        self.test_input = test_input
        self.input = input
        self.ans1 = 0
        self.ans2 = 0

    def _reset_input(self) -> None:
        self.ans1 = 0
        self.ans2 = 0

    def day(self, _input: str) -> tuple[int, int]:
        return (0, 0)

    def run(self) -> Any:
        if self.test_input:
            for index, test in enumerate(self.test_input):
                self._reset_input()
                print(f"Day {self.day_number} - Test {index + 1}: {self.day(test)}")
        if self.input:
            print(f"Day {self.day_number} - Result: {self.day(self.input)}")
