class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        res = []
        if n < m:
            return
        s_ct = [0] * 26
        p_ct = [0] * 26

        for i in range(m):
            p_ct[ord(p[i]) - ord('a')] += 1
            s_ct[ord(s[i]) - ord('a')] += 1
        if p_ct == s_ct:
            res.append(0)

        for i in range(m, n):
            s_ct[ord(s[i]) - ord('a')] += 1
            s_ct[ord(s[i - m]) - ord('a')] -= 1
            if s_ct == p_ct:
                res.append(i - m + 1)

        return res
