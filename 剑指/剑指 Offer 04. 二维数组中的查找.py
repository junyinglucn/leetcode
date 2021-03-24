class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        hi = len(matrix)
        wid = len(matrix[0])

        row = hi - 1
        col = 0

        while row >= 0 and col < wid:
            if target < matrix[row][col]:
                row -= 1
            elif target > matrix[row][col]:
                col += 1
            else:
                return True

        return False
