from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = height[:]
        stack = []
        top = [0, 0]
        for i, value in enumerate(height):
            while stack and stack[-1][1] < value:
                top = stack.pop()

            if stack:
                leftmost = stack[-1]
                for j in range(leftmost[0] + 1, i):
                    trapped[j] = value
            else:
                leftmost = top
                for j in range(leftmost[0] + 1, i):
                    trapped[j] = leftmost[1]

            stack.append([i, value])

        answer = 0
        for i, value in enumerate(trapped):
            answer += value - height[i]
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.trap([1, 0, 2, 1, 0, 1, 3, 1, 1, 2]))
    print(solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(solution.trap([4, 2, 0, 3, 2, 5]))
    print(solution.trap([4, 2, 3]))
    print(solution.trap([0, 7, 1, 4, 6]))
    print(solution.trap([3, 9, 2, 2, 8, 8, 7, 3]))
    print(solution.trap([4, 2, 0, 3, 2, 4, 3, 4]))
