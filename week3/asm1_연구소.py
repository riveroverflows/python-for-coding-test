import sys
from collections import deque, Counter
from itertools import combinations


def my_combinations(iterable, k):
    results = []

    def backtrack(start, curr):
        if len(curr) == k:
            results.append(curr[:])
            return

        for i in range(start, len(iterable)):
            curr.append(iterable[i])
            backtrack(i + 1, curr)
            curr.pop()

    backtrack(0, [])
    return results


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
        cr, cc = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < m:
                if copied_board[nr][nc] == 0:
                    copied_board[nr][nc] = 2
                    queue.append((nr, nc))

    count = Counter([])
    for row in copied_board:
        count += Counter(row)
        answer = max(answer, count[0])


for new_wall in my_combinations(empty_spaces, 3):
    for r, c in new_wall:
        board[r][c] = 1
    bfs()
    for r, c in new_wall:
        board[r][c] = 0

print(answer)
