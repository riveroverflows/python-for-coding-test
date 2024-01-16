import copy


def solution(rc, operations):
    def rotate(matrix):
        row_len = len(matrix)
        col_len = len(matrix[0])
        copied = copy.deepcopy(matrix)

        # 첫행
        for i in range(col_len - 1):
            copied[0][i + 1] = matrix[0][i]

        # 마지막행
        for i in range(col_len - 1, 0, -1):
            copied[row_len - 1][i - 1] = matrix[row_len - 1][i]

        # 첫번째 열
        for i in range(row_len - 1, 0, -1):
            copied[i - 1][0] = matrix[i][0]

        # 마지막 열
        for i in range(row_len - 1):
            copied[i + 1][col_len - 1] = matrix[i][col_len - 1]

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
