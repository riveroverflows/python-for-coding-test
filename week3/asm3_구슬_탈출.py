import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]

answer = 0
rr, rc, br, bc = 0, 0, 0, 0
queue = deque()
visited = set()

for r in range(n):
    for c in range(m):
        if board[r][c] == "R":
            rr, rc = r, c
            continue
        if board[r][c] == "B":
            br, bc = r, c

visited.add((rr, rc, br, bc))
queue.append((rr, rc, br, bc, 1))


def move(cr, cc, dr, dc):
    move_count = 0
    while board[cr + dr][cc + dc] != "#" and board[cr][cc] != "O":
        cr += dr
        cc += dc
        move_count += 1
    return cr, cc, move_count


while queue:
    cu_rr, cu_rc, cu_br, cu_bc, count = queue.popleft()
    if count > 10:
        break
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        n_rr, n_rc, r_count = move(cu_rr, cu_rc, dr, dc)
        n_br, n_bc, b_count = move(cu_br, cu_bc, dr, dc)

        if board[n_br][n_bc] == "O":
            continue

        if (n_rr, n_rc, n_br, n_bc) in visited:
            continue

        if board[n_rr][n_rc] == "O":
            answer = 1
            break

        if n_rr == n_br and n_rc == n_bc:
            if r_count > b_count:
                n_rr -= dr
                n_rc -= dc
            else:
                n_br -= dr
                n_bc -= dc

        visited.add((n_rr, n_rc, n_br, n_bc))
        queue.append((n_rr, n_rc, n_br, n_bc, count + 1))

    if answer == 1:
        break

print(answer)
