# solution A
class Solution:
    def sortByBits(self, arr):
        res = []
        d = {}
        for i in arr:
            t = str(bin(i))
            n = t.count('1')
            if n not in d:
                d[n] = []
            d[n].append(i)
        for i in sorted(d):
            res += sorted(d[i])
        return res


# solution B
class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda i: str(bin(i)).count('1') + i / 1e10)
