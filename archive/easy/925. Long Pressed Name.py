# Solution A
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        name += "1"
        for s in typed:
            if s == name[i]:
                i += 1
            elif s != name[i - 1]:
                return False
        return i == len(name) - 1


# Solution B
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        m, n = len(name), len(typed)
        while j < n:
            if i < m and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j - 1] != typed[j]:
                return False
            j += 1
        return i == m
