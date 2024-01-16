import itertools
from math import inf
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        comb = itertools.combinations(nums, len(nums) // 2)
        minimum = inf
        for com in comb:
            copy = nums[:]
            for c in com:
                copy.remove(c)
            comsum = sum(com)
            copysum = sum(copy)
            diff = comsum - copysum
            if diff == 0:
                return 0
            if diff == minimum:
                continue
            minimum = min(minimum, abs(diff))
        return minimum


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDifference([2, -1, 0, 4, -2, -9]))
    print(solution.minimumDifference([-36, 36]))
    print(solution.minimumDifference([3, 9, 7, 3]))
    print(solution.minimumDifference([27, 25, 32, 25, -71, -2]))
    print(
        solution.minimumDifference(
            [
                7772197,
                4460211,
                -7641449,
                -8856364,
                546755,
                -3673029,
                527497,
                -9392076,
                3130315,
                -5309187,
                -4781283,
                5919119,
                3093450,
                1132720,
                6380128,
                -3954678,
                -1651499,
                -7944388,
                -3056827,
                1610628,
                7711173,
                6595873,
                302974,
                7656726,
                -2572679,
                0,
                2121026,
                -5743797,
                -8897395,
                -9699694,
            ]
        )
    )
