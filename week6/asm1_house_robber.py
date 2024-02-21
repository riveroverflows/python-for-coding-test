from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = dict()
        memo[0] = nums[0]

        def dp(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                memo[i] = max(dp(i - 2) + nums[i], dp(i - 1))
            return memo[i]

        return dp(n - 1)


if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(nums=[1, 2, 3, 1]))
    print(solution.rob(nums=[2, 7, 9, 3, 1]))
