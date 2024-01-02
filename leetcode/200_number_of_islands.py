from collections import deque
from typing import List


class Solution:
    @staticmethod
    def num_islands(grid: List[List[str]]) -> int:
        answer = 0
        row = len(grid)
        col = len(grid[0])
        visited = [[False] * col for _ in range(row)]

        def bfs(x, y):
            dxdy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited[x][y] = True

            queue = deque()
            queue.append((x, y))
            while queue:
                cur_x, cur_y = queue.popleft()
                for dx, dy in dxdy:
                    next_x = cur_x + dx
                    next_y = cur_y + dy
                    if 0 <= next_x < row and 0 <= next_y < col:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True
                            queue.append((next_x, next_y))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    answer += 1

        return answer


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(Solution.num_islands(grid1))
print(Solution.num_islands(grid2))
