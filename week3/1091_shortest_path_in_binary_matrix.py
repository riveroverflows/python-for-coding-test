from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(r, c, d):
            q = deque()
            q.append((r, c, d))
            visited[r][c] = True

            next_d = 0
            while q:
                cur_r, cur_c, cur_d = q.popleft()
                if (cur_r, cur_c) == (n - 1, n - 1):
                    return cur_d
                next_d = cur_d + 1

                for dr, dc in directions:
                    next_r = cur_r + dr
                    next_c = cur_c + dc
                    if 0 <= next_r < n and 0 <= next_c < n:
                        if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                            q.append((next_r, next_c, next_d))
                            visited[next_r][next_c] = True

            if (r, c) != (n - 1, n - 1):
                return -1
            return next_d

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
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

    grid = [[0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # 14

    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # 14

    grid = [[0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))  # -1
