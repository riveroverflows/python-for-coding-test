from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i, num in enumerate(nums):
            nums_dict[num] = i

        for i, num in enumerate(nums):
            need = target - num
            if num == need and nums.count(num) == 2:
                return [i, nums.index(need, i + 1)]
            need_index = nums_dict.get(need, None)
            i_index = nums_dict.get(num)
            if need_index and need_index != i_index:
                return [i_index, need_index]


print(Solution.two_sum([4, 1, 9, 7, 5, 3, 16], 14))
print(Solution.two_sum([2, 1, 5, 7], 4))
print(Solution.two_sum([2, 7, 11, 15], 9))
print(Solution.two_sum([3, 2, 4], 6))
print(Solution.two_sum([3, 3], 6))
print(Solution.two_sum([3, 5, 2, 3, 9], 10))
print(Solution.two_sum([3, 5, 2, 2, 1, 9], 10))
