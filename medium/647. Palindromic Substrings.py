# Solution A
class Solution:
    def countSubstrings(self, s):
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                char = s[i:j + 1]
                if char == char[::-1]:
                    count += 1
        return count


# Solution B
class Solution:
    def countSubstrings(self, s):
        res = 0
        for i in range(len(s)):
            res += self.check(s, i, i)
            res += self.check(s, i, i + 1)
        return res

    def check(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        return count
