# Solution A
class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[j] == s[i]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    max_tmp = j - i + 1
                    if max_tmp > max_len:
                        max_len = max_tmp
                        start = i
        return s[start:start + max_len]

# Solution B
class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.center_spread(s, size, i, i)
            palindrome_even, even_len = self.center_spread(s, size, i, i + 1)

            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub

        return res

    def center_spread(self, s, size, left, right):
        i = left
        j = right

        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1:j], j - i - 1