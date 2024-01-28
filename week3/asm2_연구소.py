import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 0: 빈 칸 / 1: 벽 / 2: 바이러스
answer = 100000
viruses = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 2:
            viruses.append((r, c))


def bfs(active_viruses):
    global answer
    copied_board = [board[i][:] for i in range(n)]
    queue = deque()
    for r, c in active_viruses:
        queue.append((r, c, 0))

    count = 0
    while queue:
        cr, cc, cl = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc, nl = cr + dr, cc + dc, cl + 1
            if 0 <= nr < n and 0 <= nc < n:
                if copied_board[nr][nc] == 0:
                    copied_board[nr][nc] = 3
                    count = max(count, nl)
                    queue.append((nr, nc, nl))
                elif copied_board[nr][nc] == 2:
                    copied_board[nr][nc] = 3
                    queue.append((nr, nc, nl))

    for r in range(n):
        for c in range(n):
            if copied_board[r][c] == 0:
                return

    answer = min(answer, count)
    return


for active_viruses in combinations(viruses, m):
    for r, c in active_viruses:
        board[r][c] = 3
    bfs(active_viruses)
    for r, c in active_viruses:
        board[r][c] = 2

if answer == 100000:
    answer = -1

print(answer)
