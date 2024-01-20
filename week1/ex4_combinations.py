import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answers = []

        def backtrack(start, curr):
            if len(curr) == k:
                answers.append(curr[:])
                return

            for i in range(start, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(1, [])
        return answers


if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(5, 3))
    print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))
