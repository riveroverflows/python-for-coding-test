from collections import deque

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def get_next_positions(position, board):
    (r1, c1), (r2, c2) = position
    positions = []

    for dr, dc in directions:
        next_r1, next_c1 = r1 + dr, c1 + dc
        next_r2, next_c2 = r2 + dr, c2 + dc
        if board[next_r1][next_c1] == 0 and board[next_r2][next_c2] == 0:
            positions.append(((next_r1, next_c1), (next_r2, next_c2)))

    # 가로
    if r1 == r2:
        if board[r1 - 1][c1] == 0 and board[r2 - 1][c2] == 0:
            positions.append(((r1, c1), (r1 - 1, c1)))
            positions.append(((r2 - 1, c2), (r2, c2)))
        if board[r1 + 1][c1] == 0 and board[r2 + 1][c2] == 0:
            positions.append(((r1, c1), (r1 + 1, c1)))
            positions.append(((r2 + 1, c2), (r2, c2)))

    # 세로
    if c1 == c2:
        if board[r1][c1 - 1] == 0 and board[r2][c2 - 1] == 0:
            positions.append(((r1, c1), (r1, c1 - 1)))
            positions.append(((r2, c2 - 1), (r2, c2)))
        if board[r1][c1 + 1] == 0 and board[r2][c2 + 1] == 0:
            positions.append(((r1, c1), (r1, c1 + 1)))
            positions.append(((r2, c2 + 1), (r2, c2)))

    return positions


def solution(board):
    n = len(board)
    grid = [[1] * (n + 2) for _ in range(n + 2)]
    for r in range(n):
        for c in range(n):
            grid[r + 1][c + 1] = board[r][c]

    position = ((1, 1), (1, 2))
    distance = 0

    queue = deque()
    queue.append((position, distance))
    visited = set()
    visited.add(position)

    while queue:
        curr_position, curr_distance = queue.popleft()
        if (n, n) in curr_position:
            return curr_distance

        for next_position in get_next_positions(curr_position, grid):
            if next_position not in visited:
                queue.append((next_position, curr_distance + 1))
                visited.add(next_position)


print(
    solution(board=[
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0]]
    )
)
