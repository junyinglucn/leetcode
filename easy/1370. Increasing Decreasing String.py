class Solution:
    def sortString(self, s):
        res = ''
        while len(set(s)) > 0:
            res += ''.join(sorted(set(s)))
            for c in set(s):
                s = s.replace(c, '', 1)
            res += ''.join(sorted(set(s))[::-1])
            for c in set(s):
                s = s.replace(c, '', 1)
        return res