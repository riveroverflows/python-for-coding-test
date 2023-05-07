import itertools
from typing import List


class Solution:
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        answer = list()
        for p in itertools.permutations(nums):
            answer.append(list(p))
        return answer
    # return list(itertools.permutations(nums))  이것도 성공함


print(Solution.permute([1, 2, 3]))
print(Solution.permute([0, 1]))
print(Solution.permute([1]))
