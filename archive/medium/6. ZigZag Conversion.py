class Solution:
    def convert(self, s, numRows):
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i = 0
        flag = -1
        for w in s:
            res[i] += w
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
        return "".join(res)
