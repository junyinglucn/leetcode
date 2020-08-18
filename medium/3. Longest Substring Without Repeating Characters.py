# Solution A
class Solution:
    def lengthOfLongestSubstring(self, s):
        sub = set()
        n = len(s)
        r = -1
        res = 0
        for i in range(n):
            if i != 0:
                sub.remove(s[i - 1])
            while r + 1 < n and s[r + 1] not in sub:
                sub.add(s[r + 1])
                r += 1
            res = max(res, r - i + 1)
        return res


# Solution B
class Solution:
    def lengthOfLongestSubstring(self, s):
        res = 0
        for idx, x in enumerate(s):
            for idy, y in enumerate(s[idx:], idx):
                if y in s[idx:idy]:
                    res = max(res, idy - idx)
                    break
                elif idy == len(s) - 1:
                    res = max(res, idy - idx + 1)
        return res
