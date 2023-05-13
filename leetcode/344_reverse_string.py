from typing import List


class Solution:
    @staticmethod
    def reverse_string(s: List[str]) -> None:
        for i in range(len(s) // 2):
            back = -(i + 1)
            s[i], s[back] = s[back], s[i]


s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]
Solution.reverse_string(s1)
Solution.reverse_string(s2)
print(s1)
print(s2)
