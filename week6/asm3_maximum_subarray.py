from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(solution.maxSubArray(nums=[1]))
    print(solution.maxSubArray(nums=[5, 4, -1, 7, 8]))
