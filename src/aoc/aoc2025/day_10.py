from typing import Any
from ..utils.day import Day
from ..utils import aoc
import re
import heapq
from z3 import *


def find_sum_target(equivalent_buttons: list[int], target: int) -> list[int]:
    n_buttons = len(equivalent_buttons)
    n = len(target)
    opt = Optimize()

    count = [Int(f"count_{i}") for i in range(n_buttons)]
    for c in count:
        opt.add(c >= 0, c <= 100000)

    for j in range(n):
        opt.add(Sum(count[i] * equivalent_buttons[i][j] for i in range(n_buttons)) == target[j])

    total_used = Sum(count)
    opt.minimize(total_used)

    if opt.check() != sat:
        return None

    model = opt.model()
    counts = [model.evaluate(c).as_long() for c in count]
    return counts



class Day10(Day):

    def day(self, _input: str) -> Any:
        lights, buttons, joltage = [], [], []
        for line in aoc.yield_line(_input):
            lights.append(list(re.search(r'\[(.*?)\]', line).group(1)))
            buttons.append([list(map(int, group.split(','))) for group in re.findall(r'\((.*?)\)', line)])
            joltage.append(list(map(int, re.search(r'\{(.*?)\}', line).group(1).split(','))))

        for target_1, allowed_buttons, target_2 in [(lights[i], buttons[i], joltage[i]) for i in range(len(lights))]:

            current_queue = []
            heapq.heappush(current_queue, (0, set()))

            while True:
                assert len(current_queue) != 0 and current_queue is not None
                current_used = heapq.heappop(current_queue)[1]

                current_target = ["." for _ in range(len(target_1))]
                for bs in current_used:
                    for button in allowed_buttons[bs]:
                        current_target[button] = "#" if current_target[button] == "." else "."

                if current_target == target_1:
                    self.ans1 += len(current_used)
                    break

                for i in range(len(allowed_buttons)):
                    if i not in current_used:
                        new_used = current_used.copy()
                        new_used.add(i)
                        heapq.heappush(current_queue, (len(new_used), new_used))

            equivalent_buttons = []
            for bs in allowed_buttons:
                new_array = [0 for _ in range(len(target_2))]
                for button in bs:
                    new_array[button] = 1
                equivalent_buttons.append(new_array)

            self.ans2 += sum(find_sum_target(equivalent_buttons, target_2))




        return (self.ans1, self.ans2)

