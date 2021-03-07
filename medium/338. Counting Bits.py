# Solution A
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num + 1):
            res.append(bin(i).count("1"))
        return res


# Solution B
class Solution:
    def countBits(self, num):
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits
