class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        if l == 0:
            return 0
        i = 0
        while i <= (len(haystack) - l):
            if haystack[i:i + l] == needle:
                return i
            i += 1
        return -1
