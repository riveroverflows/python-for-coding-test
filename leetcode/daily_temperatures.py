from typing import List


class Solution:
    @staticmethod
    def daily_temperatures(temperatures: List[int]) -> List[int]:
        stack = list()
        answer = [0 for _ in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            if not stack or t < stack[-1][1]:
                stack.append([i, t])
                continue
            while stack and t > stack[-1][1]:
                temperature = stack.pop()
                answer[temperature[0]] = i - temperature[0]
            stack.append([i, t])
        return answer


print(Solution.daily_temperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
print(Solution.daily_temperatures(temperatures=[30, 40, 50, 60]))
print(Solution.daily_temperatures(temperatures=[30, 60, 90]))
