import itertools
from typing import List


class Solution:
    def met_the_queen(self, n, r, c, dr, dc, chessboard):
        # 다음 위치가 Q가 아니면 ok
        while 0 <= r < n and 0 <= c < n:
            if chessboard[r][c] == "Q":
                return True
            r += dr
            c += dc
        return False

    def solveNQueens(self, n: int) -> List[List[str]]:
        chess_rc = []
        for r in range(n):
            for c in range(n):
                chess_rc.append((r, c))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        answer = []
        for queens in itertools.combinations(chess_rc, n):
            # 보드 초기화
            chessboard = [["."] * n for _ in range(n)]

            # 퀸 좌표 입력
            for queen in queens:
                qr, qc = queen
                chessboard[qr][qc] = "Q"

            met_the_queen = False
            for queen in queens:
                qr, qc = queen
                for dr, dc in directions:
                    nr, nc = qr + dr, qc + dc
                    # 보드판 범위 확인
                    # Q 만났으면 break
                    if self.met_the_queen(n, nr, nc, dr, dc, chessboard):
                        met_the_queen = True
                        break
            if not met_the_queen:
                board = []
                for row in chessboard:
                    board.append("".join(row))
                answer.append(board)

        return answer


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(n=6))
