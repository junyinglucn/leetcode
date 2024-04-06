class Solution:
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        res = [[1]]
        row_last = [1]
        for i in range(2, rowIndex + 2):
            row_now = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    row_now.append(1)
                else:
                    row_now.append(row_last[j - 1] + row_last[j])
            res.append(row_now)
            row_last = row_now
        return res[-1]