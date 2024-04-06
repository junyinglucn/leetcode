# Solution A
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        for i in range(min(len(matrix), len(matrix[0]))):
            vf = self.search(matrix, i, target, True)
            hf = self.search(matrix, i, target, False)
            if vf or hf:
                return True
        return False

    def search(self, matrix, start, target, vertical):
        low = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while hi >= low:
            mid = (hi + low) // 2
            if vertical:
                if matrix[start][mid] > target:
                    hi = mid - 1
                elif matrix[start][mid] < target:
                    low = mid + 1
                else:
                    return True
            else:
                if matrix[mid][start] > target:
                    hi = mid - 1
                elif matrix[mid][start] < target:
                    low = mid + 1
                else:
                    return True
        return False


# Solution B
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def search(up, down, left, right):
            if left > right or up > down:
                return False
            elif target > matrix[down][right] or target < matrix[up][left]:
                return False
            mid = left + (right - left) // 2
            row = up
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1
            return search(row, down, left, mid - 1) or search(up, row - 1, mid + 1, right)

        return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

# Solution C
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        hi = len(matrix)
        wid = len(matrix[0])

        row = hi - 1
        col = 0

        while row >= 0 and col < wid:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True

        return False
