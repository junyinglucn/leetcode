# Solution A
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != tmp:
                    return strs[0][:i]
        return strs[0]


# Solution B
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        s1 = min(strs)
        s2 = max(strs)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1
