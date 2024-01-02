import itertools


class Solution:
    @staticmethod
    def get_permutation(n: int, k: int) -> str:
        permutations = itertools.permutations(range(1, n + 1))
        for i, value in enumerate(permutations):
            if k != i + 1:
                continue
            return "".join(list(map(str, value)))


print(Solution.get_permutation(3, 3))
