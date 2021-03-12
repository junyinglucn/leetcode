class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xory = x ^ y
        dis = 0
        while xory:
            if xory & 1:
                dis += 1
            xory = xory >> 1
        return dis
