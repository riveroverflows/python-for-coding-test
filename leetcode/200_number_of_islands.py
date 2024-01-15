from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        visited = [[False] * col_len for _ in range(row_len)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited[r][c] = True

            while q:
                cur_r, cur_c = q.popleft()
                for dr, dc in directions:
                    next_r = cur_r + dr
                    next_c = cur_c + dc
                    if 0 <= next_r < row_len and 0 <= next_c < col_len and grid[next_r][next_c] == "1":
                        if not visited[next_r][next_c]:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True

        answer = 0
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    answer += 1
        return answer


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    solution = Solution()
    print(solution.numIslands(grid))

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    print(solution.numIslands(grid))
