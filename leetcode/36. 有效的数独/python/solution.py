from typing import List
from itertools import islice


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            check_list = [False] * 10
            for num in row:
                if num == '.':
                    continue
                if check_list[int(num)]:
                    return False
                check_list[int(num)] = True
        for col in range(0, 9):
            check_list = [False] * 10
            for row in board:
                if row[col] == '.':
                    continue
                if check_list[int(row[col])]:
                    return False
                check_list[int(row[col])] = True

        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                check_list = [False] * 10
                for row in islice(board, row_start, row_start + 3):
                    for col in range(col_start, col_start + 3):
                        if row[col] == '.':
                            continue
                        if check_list[int(row[col])]:
                            return False
                        check_list[int(row[col])] = True
        return True
