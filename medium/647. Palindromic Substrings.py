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


# Solution C
class Solution:
    def countSubstrings(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0
        for j in range(n):
            for i in range(0, j + 1):
                length = j - i + 1
                if length == 1:
                    dp[i][j] = True
                    count += 1
                if length == 2 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                    count += 1
        return count


# Solution D
class Solution:
    def countSubstrings(self, s):
        s = '#' + '#'.join(s) + '#'
        r = -1
        maxlen = [0] * len(s)
        res = 0
        for i in range(len(s)):
            if i <= r:
                im = 2 * j - i
                minlen = min(maxlen[im], r - i)
                tmp = self.check(s, i - minlen, i + minlen)
            else:
                tmp = self.check(s, i, i)
            maxlen[i] = tmp
            if i + tmp > r:
                r = i + tmp
                j = i
            if i % 2 == 1:
                res += maxlen[i] // 2 + i
            else:
                res += (maxlen[i] + 1) // 2
        return res

    def check(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (r - 1) // 2 - 1
