from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def backtrack():
            print()

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    continue
                num = 1

                print(board[i][j], end="")
            print()


if __name__ == "__main__":
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
