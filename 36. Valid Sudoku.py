class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows_map = {i: set() for i in range(9)}
        columns_map = {i: set() for i in range(9)}
        block_map = {}
        for row in range(9):
            for column in range(9):
                digit = board[row][column]
                if digit == '.':
                    continue

                block_area = (row // 3, column // 3)
                if not block_area in block_map:
                    block_map[block_area] = set()

                if (
                   digit in rows_map[row] 
                   or digit in columns_map[column]
                   or digit in block_map[block_area]
                ):
                    return False
                
                rows_map[row].add(digit)
                columns_map[column].add(digit)
                block_map[block_area].add(digit)

        return True

print(Solution().isValidSudoku(
    [[".","8","7","6","5","4","3","2","1"],
    ["2",".",".",".",".",".",".",".","."],
    ["3",".",".",".",".",".",".",".","."],
    ["4",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".",".","."],
    ["6",".",".",".",".",".",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    ["8",".",".",".",".",".",".",".","."],
    ["9",".",".",".",".",".",".",".","."]]
))