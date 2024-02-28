"""
https://www.acmicpc.net/problem/17142
"""
import sys
from collections import deque
from itertools import combinations
from math import inf

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input().split()) for _ in range(n)]
answer = inf
# 0 빈 칸 / 1 벽 / 2 바이러스
viruses = []
for r in range(n):
    for c in range(n):
        if grid[r][c] == "2":
            viruses.append((r, c))


def bfs(active_viruses):
    global answer
    copied_grid = [grid[i][:] for i in range(n)]
    queue = deque()
    for vr, vc in active_viruses:
        copied_grid[vr][vc] = "3"
        queue.append((vr, vc, 0))

    count = 0
    while queue:
        cr, cc, cs = queue.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc, ns = cr + dr, cc + dc, cs + 1
            if 0 <= nr < n and 0 <= nc < n:
                if copied_grid[nr][nc] == "0":
                    copied_grid[nr][nc] = "3"
                    count = max(count, ns)
                    queue.append((nr, nc, ns))
                elif copied_grid[nr][nc] == "2":
                    copied_grid[nr][nc] = "3"
                    queue.append((nr, nc, ns))

    for r in range(n):
        for c in range(n):
            if copied_grid[r][c] == "0":
                return
    answer = min(count, answer)


for active_viruses in combinations(viruses, m):
    bfs(active_viruses)

if answer == inf:
    answer = -1

print(answer)
