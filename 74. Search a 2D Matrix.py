class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        MAX_ROW, MAX_COLUMN = len(matrix) - 1, len(matrix[0]) - 1
        
        # find row target could be
        up, bottom = 0, MAX_ROW
        while up < bottom:
            # upper bound
            middle = (up + bottom) >> 1

            if target > matrix[middle][MAX_COLUMN]:
                up = middle + 1
            else:
                bottom = middle

        target_row = bottom
        if not (matrix[target_row][0] <= target <= matrix[target_row][MAX_COLUMN]):
            return False

        # Search the target in row
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            middle = (left + right) >> 1

            if target > matrix[target_row][middle]:
                left = middle + 1
            else:
                right = middle
        return matrix[target_row][left] == target