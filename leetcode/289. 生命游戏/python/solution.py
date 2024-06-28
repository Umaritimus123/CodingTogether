from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        活 -> 死 活少于2或大于3
        活 -> 活 2或3活
        死 -> 活 3活
        """
        for row, line in enumerate(board):
            for col, life in enumerate(line):
                count = 0
                for r in range(max(row - 1, 0), min(row + 2, len(board))):
                    for c in range(max(col - 1, 0), min(col + 2, len(line))):
                        surrounding_life = board[r][c]
                        if surrounding_life & 1 == 1: # 本活
                            count += 1
                if life & 1 == 1: # 本活
                    if count in (3, 4):
                        board[row][col] |= 2
                else:
                    if count == 3:
                        board[row][col] |= 2
        for row, line in enumerate(board):
            for col, _ in enumerate(line):
                board[row][col] >>= 1
