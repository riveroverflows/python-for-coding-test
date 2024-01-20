import itertools
from typing import List


class Solution:
    # 순열은 순서가 중요해~ 수의 조합 자체는 겹쳐도 되지만 수의 순서가 중요하다~
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = []

        def backtrack(curr):
            if len(curr) == len(nums):
                answers.append(curr[:])
                return
            for num in nums:
                if num in curr:
                    continue
                curr.append(num)
                backtrack(curr)
                curr.pop()

        backtrack([])
        return answers


if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    print(list(itertools.permutations([1, 2, 3])))
