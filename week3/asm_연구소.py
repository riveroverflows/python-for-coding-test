"""
https://www.acmicpc.net/problem/14502
"""
import sys
from collections import deque, Counter
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input().split()) for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
empty_spaces, viruses = [], []
answer = 0

for r in range(n):
    for c in range(m):
        if grid[r][c] == "0":
            empty_spaces.append((r, c))
        elif grid[r][c] == "2":
            viruses.append((r, c))


def bfs(new_walls):
    global answer
    copied_grid = [grid[i][:] for i in range(n)]
    for nwr, nwc in new_walls:
        copied_grid[nwr][nwc] = "1"

    queue = deque(viruses)

    while queue:
        cr, cc = queue.popleft()
        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m:
                if copied_grid[nr][nc] == "0":
                    copied_grid[nr][nc] = "2"
                    queue.append((nr, nc))

    count = Counter([])
    for row in copied_grid:
        count += Counter(row)
    answer = max(answer, count["0"])


for new_walls in combinations(empty_spaces, 3):
    bfs(new_walls)

print(answer)
