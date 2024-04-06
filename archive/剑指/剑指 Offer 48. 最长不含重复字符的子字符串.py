class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = -1
        res = 0
        dic = {}
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i, dic[s[j]])
            dic[s[j]] = j
            res = max(res, j - i)
        return res
