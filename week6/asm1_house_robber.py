from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]

        if n > 1:
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[n - 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.rob(nums=[1, 2, 3, 1]))
    print(solution.rob(nums=[2, 7, 9, 3, 1]))
