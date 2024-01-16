from typing import List


class Solution:
    @staticmethod
    def partition(s: str) -> List[List[str]]:
        results = list()
        for i in range(1, len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                print()
        return [[]]


print(Solution.partition("abc"))
