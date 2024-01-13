import copy
from collections import deque


def solution(rc, operations):
    def rotate(matrix):
        copied = copy.deepcopy(matrix)
        row = len(matrix)
        col = len(matrix[0])
        visited = [[False] * col for _ in range(row)]
        for i in range(1, row - 1):
            for j in range(1, col - 1):
                visited[i][j] = True

        def bfs(x, y):
            q = deque()
            q.append((x, y))
            visited[x][y] = True

            while q:
                cur_x, cur_y = q.popleft()
                if cur_x == 0:
                    for next_y in range(cur_y + 1, col):
                        copied[cur_x][next_y] = matrix[cur_x][next_y - 1]
                elif cur_x == row - 1:
                    for next_y in range(col - 1, 0, -1):
                        copied[cur_x][next_y - 1] = matrix[cur_x][next_y]
                else:
                    if cur_y == 0:
                        for next_x in range(row - 1, 0, -1):
                            copied[next_x - 1][cur_y] = matrix[next_x][cur_y]
                    if cur_y == col - 1:
                        for next_x in range(cur_x, row):
                            copied[next_x][cur_y] = matrix[next_x - 1][cur_y]

        for i in range(row):
            for j in range(col):
                if not visited[i][j]:
                    bfs(i, j)

        return copied

    def shiftrow(matrix):
        copied = [0] * len(matrix)
        for i, row in enumerate(matrix):
            if i + 1 >= len(matrix):
                copied[0] = row
            else:
                copied[i + 1] = row
        return copied

    answer = rc
    for op in operations:
        if "Rotate" == op:
            answer = rotate(answer)
        if "ShiftRow" == op:
            answer = shiftrow(answer)
    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
