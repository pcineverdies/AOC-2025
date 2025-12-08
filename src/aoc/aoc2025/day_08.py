from typing import Any
from ..utils.day import Day
from ..utils import aoc
from scipy.cluster.hierarchy import DisjointSet

def distance(t1: tuple, t2: tuple) -> int:
    return ((t1[0] - t2[0])**2) + ((t1[1] - t2[1])**2) + ((t1[2] - t2[2])**2)

class Day08(Day):

    def day(self, _input: str) -> Any:
        coordinates, distance_pair = [], []
        for idx, line in enumerate(aoc.yield_line(_input)):
            nums = aoc.str_to_list_int(line)
            new_coordinate = (nums[0], nums[1], nums[2])
            for i in range(len(coordinates)):
                distance_pair.append((distance(coordinates[i], new_coordinate), (i, idx)))
            coordinates.append(new_coordinate)

        distance_pair = sorted(distance_pair, key=lambda x: x[0])
        disjoint_set = DisjointSet(range(len(coordinates)))

        for i in range(100000000):
            disjoint_set.merge(distance_pair[i][1][0], distance_pair[i][1][1])
            if i == 1000:
                sets = sorted(disjoint_set.subsets(), key=lambda x: -len(x))
                self.ans1 = len(sets[0]) * len(sets[1]) * len(sets[2])
            if disjoint_set.subset_size(0) == len(coordinates):
                self.ans2 = coordinates[distance_pair[i][1][0]][0] * coordinates[distance_pair[i][1][1]][0]
                break

        return (self.ans1, self.ans2)

