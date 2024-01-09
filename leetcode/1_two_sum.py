from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        copied_nums = nums[:]
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                left_idx = copied_nums.index(nums[left])
                right_idx = list(filter(lambda x: copied_nums[x] == nums[right], range(len(nums))))[-1]
                return [left_idx, right_idx]
            if nums[left] + nums[right] < target:
                left += 1
            if nums[left] + nums[right] > target:
                right -= 1


if __name__ == "__main__":
    print(Solution.two_sum([2, 7, 11, 15], 9))
    print(Solution.two_sum([3, 2, 4], 6))
    print(Solution.two_sum([3, 3], 6))
