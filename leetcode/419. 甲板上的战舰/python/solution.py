from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
            一遍扫描，额外空间O(1)。
        """
        ship_num = 0
        for row, line in enumerate(board):
            for col, cell in enumerate(line):
                if cell == '.':
                    continue
                if ((row == 0 or board[row - 1][col] != 'X') and
                    (col == 0 or board[row][col - 1] != 'X')):
                    ship_num += 1 # 检查每一个单元格，如果是X，只要额外检查其左边和上边均没有X则可计数一次ship。
        return ship_num


if __name__ == '__main__':
    board = [
        ["X",".",".","X"],
        [".",".",".","X"],
        [".",".",".","X"],
    ]
    print(Solution().countBattleships(board))
