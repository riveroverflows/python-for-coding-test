import copy


def solution(rc, operations):
    def rotate(matrix):
        copied = copy.deepcopy(matrix)
        row_len = len(matrix)
        col_len = len(matrix[0])
        news = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        start_r, start_c = 0, 0
        start_v = matrix[start_r][start_c]

        for i in {0, row_len - 1}:
            for j in range(col_len):
                copied[i][j] = -1
        for i in {0, col_len - 1}:
            for j in range(row_len):
                copied[j][i] = -1

        def is_valid(r, c):
            return 0 <= r < row_len and 0 <= c < col_len and copied[r][c] == -1

        def dfs(r, c, v):
            for dr, dc in news:
                next_r = r + dr
                next_c = c + dc
                if is_valid(next_r, next_c):
                    if copied[next_r][next_c] == -1:
                        copied[next_r][next_c] = v
                        next_v = matrix[next_r][next_c]
                        dfs(next_r, next_c, next_v)

        dfs(start_r, start_c, start_v)
        return copied

    def shift_row(matrix):
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
            answer = shift_row(answer)
    return answer


print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate"]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]))
