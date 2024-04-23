import itertools
import sys
from collections import Counter, deque
from math import inf

input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

empty_spaces = []
viruses = []
for r in range(n):
    for c in range(m):
        if lab[r][c] == 0:
            empty_spaces.append((r, c))
        elif lab[r][c] == 2:
            viruses.append((r, c))

answer = -inf
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(new_walls):
    global answer
    new_lab = [lr[:] for lr in lab]
    for wr, wc in new_walls:
        new_lab[wr][wc] = 1

    queue = deque(viruses)
    while queue:
        vr, vc = queue.popleft()
        for dr, dc in directions:
            nr, nc = vr + dr, vc + dc
            if 0 <= nr < n and 0 <= nc < m:
                if new_lab[nr][nc] == 0:
                    new_lab[nr][nc] = 2
                    queue.append((nr, nc))

    counter = Counter([])
    for lr in new_lab:
        counter += Counter(lr)
    answer = max(answer, counter[0])


for new_walls in itertools.combinations(empty_spaces, 3):
    bfs(new_walls)

print(answer)
