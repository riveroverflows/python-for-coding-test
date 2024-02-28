from collections import deque
from typing import List


class Solution:
    """
    https://leetcode.com/problems/shortest-path-in-binary-matrix/
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        answer = -1

        def bfs(r, c, d):
            queue = deque()
            queue.append((r, c, d))
            visited.add((r, c))

            while queue:
                cr, cc, cd = queue.popleft()
                if (cr, cc) == (n - 1, n - 1):
                    return cd
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < n and not grid[nr][nc] and (nr, nc) not in visited:
                        queue.append((nr, nc, cd + 1))
                        visited.add((nr, nc))
            return -1

        if grid[0][0] or grid[n - 1][n - 1]:
            return answer

        return bfs(0, 0, 1)


if __name__ == "__main__":
    solution = Solution()

    grid = [[0, 1], [1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # 2

    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # 4

    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # -1

    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # 4

    grid = [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # 3

    grid = [
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
    ]
    print(solution.shortestPathBinaryMatrix(grid))  # 14

    grid = [
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0],
    ]
    print(solution.shortestPathBinaryMatrix(grid))  # 14

    grid = [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0]
    ]
    print(solution.shortestPathBinaryMatrix(grid))  # -1
