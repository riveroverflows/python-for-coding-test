from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_valid(row, col):
            # 현재 열에 퀸이 있는지 체크
            # 0부터 현재 위치 전까지
            # ex backtracking(3) -> range: 0 ~ 2
            for r in range(row):
                if chessboard[r][col] == "Q":
                    return False

            # 양 대각선 체크
            for dr, dc in [(-1, -1), (-1, 1)]:
                nr, nc = row + dr, col + dc
                while 0 <= nr < n and 0 <= nc < n:
                    if chessboard[nr][nc] == "Q":
                        return False
                    nr += dr
                    nc += dc

            # 여기까지 왔으면 valid 함
            return True

        def backtracking(row):
            if row == n:
                answer.append(["".join(r) for r in chessboard])

            # row의 열 순회
            for col in range(n):
                # chessboard[row][col] 에 Q를 위치 시켜도 되는지 확인
                if is_valid(row, col):
                    chessboard[row][col] = "Q"
                    backtracking(row + 1)
                    chessboard[row][col] = "."

        answer = []
        chessboard = [["."] * n for _ in range(n)]
        backtracking(0)
        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(n=6))
