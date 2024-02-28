from collections import deque
from typing import List


class Solution:
    """
    https://leetcode.com/problems/number-of-islands/
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        rl, cl = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                cr, cc = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rl and 0 <= nc < cl and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        answer = 0
        for out_r in range(rl):
            for out_c in range(cl):
                if grid[out_r][out_c] == "1" and (out_r, out_c) not in visited:
                    bfs(out_r, out_c)
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
