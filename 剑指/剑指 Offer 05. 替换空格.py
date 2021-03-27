class Solution:
    def replaceSpace(self, s: str) -> str:
        res = ''
        for i in s:
            if i == " ":
                i = "%20"
            res += i
        return res
