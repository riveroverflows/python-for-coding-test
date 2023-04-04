from typing import List


class Solution:
    @staticmethod
    def longest_consecutive(nums: List[int]) -> int:
        longer = 0
        nums_set = set(nums)
        for i in nums:
            count = 0
            if i - 1 not in nums_set:
                count += 1
                target = i + 1
                while target in nums_set:
                    count += 1
                    target += 1
                longer = max(longer, count)
        return longer


print(Solution.longest_consecutive([100, 4, 200, 1, 3, 2]))
print(Solution.longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
