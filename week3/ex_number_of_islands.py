from collections import deque
from typing import List


class Solution:
    """
    https://leetcode.com/problems/number-of-islands/
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited[r][c] = True
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < row_len and 0 <= nc < col_len and not visited[nr][nc] and grid[nr][nc] == "1":
                        queue.append((nr, nc))
                        visited[nr][nc] = True

        answer = 0
        for r in range(row_len):
            for c in range(col_len):
                if grid[r][c] == "1" and not visited[r][c]:
                    bfs(r, c)
                    answer += 1

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.numIslands(grid=[["1", "1", "1", "1", "0"],
                                    ["1", "1", "0", "1", "0"],
                                    ["1", "1", "0", "0", "0"],
                                    ["0", "0", "0", "0", "0"]]))

    print(solution.numIslands(grid=[["1", "1", "0", "0", "0"],
                                    ["1", "1", "0", "0", "0"],
                                    ["0", "0", "1", "0", "0"],
                                    ["0", "0", "0", "1", "1"]]))
