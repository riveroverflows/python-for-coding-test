import sys
from collections import deque, Counter
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

answer = 0
viruses, empty_spaces = [], []

for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            empty_spaces.append((r, c))
        elif board[r][c] == 2:
            viruses.append((r, c))


def bfs():
    global answer
    copied_board = [board[i][:] for i in range(n)]
    queue = deque(viruses)

    while queue:
        r, c = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_r, next_c = r + dr, c + dc
            if 0 <= next_r < n and 0 <= next_c < m:
                if copied_board[next_r][next_c] == 0:
                    copied_board[next_r][next_c] = 2
                    queue.append((next_r, next_c))

    count = Counter([])
    for row in copied_board:
        count += Counter(row)
        answer = max(answer, count[0])


for new_wall in combinations(empty_spaces, 3):
    for r, c in new_wall:
        board[r][c] = 1
    bfs()
    for r, c in new_wall:
        board[r][c] = 0

print(answer)
