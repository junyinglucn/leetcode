class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos1 = 0
        pos2 = len(matrix) - 1
        while pos1 < pos2:
            add = 0
            while add < pos2 - pos1:
                tmp = matrix[pos2 - add][pos1]
                matrix[pos2 - add][pos1] = matrix[pos2][pos2 - add]
                matrix[pos2][pos2 - add] = matrix[pos1 + add][pos2]
                matrix[pos1 + add][pos2] = matrix[pos1][pos1 + add]
                matrix[pos1][pos1 + add] = tmp
                add += 1
            pos1 += 1
            pos2 -= 1
