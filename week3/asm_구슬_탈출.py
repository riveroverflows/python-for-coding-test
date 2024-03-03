"""
https://www.acmicpc.net/problem/13459
"""
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
answer = 0
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = set()

rr, rc, br, bc = 0, 0, 0, 0
for r in range(n):
    for c in range(m):
        if board[r][c] == "R":
            rr, rc = r, c
        elif board[r][c] == "B":
            br, bc = r, c

queue = deque()
queue.append((rr, rc, br, bc, 1))
visited.add((rr, rc, br, bc))


def move_ball(cr, cc, dr, dc):
    moved_count = 0
    while board[cr + dr][cc + dc] != "#" and board[cr][cc] != "O":
        cr += dr
        cc += dc
        moved_count += 1
    return cr, cc, moved_count


def bfs():
    while queue:
        cu_rr, cu_rc, cu_br, cu_bc, move = queue.popleft()
        if move > 10:
            return 0
        for dr, dc in directions:
            nrr, nrc, rmv = move_ball(cu_rr, cu_rc, dr, dc)
            nbr, nbc, bmv = move_ball(cu_br, cu_bc, dr, dc)

            if board[nbr][nbc] == "O":
                continue

            if (nrr, nrc, nbr, nbc) in visited:
                continue

            if board[nrr][nrc] == "O":
                return 1

            if (nrr, nrc) == (nbr, nbc):
                if rmv > bmv:
                    nrr -= dr
                    nrc -= dc
                else:
                    nbr -= dr
                    nbc -= dc

            queue.append((nrr, nrc, nbr, nbc, move + 1))
            visited.add((nrr, nrc, nbr, nbc))
    return answer


print(bfs())
