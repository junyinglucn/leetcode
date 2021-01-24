class Solution:
    def numTrees(self, n: int) -> int:
        res = [1, 1]
        if n <= 1:
            return res[n]
        for i in range(2, n + 1):
            s = i - 1
            ct = 0
            for j in range(i):
                ct += res[s - j] * res[j]
            res.append(ct)
        return res[n]
