class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        charS = []
        charT = []
        for i in S:
            if i != '#':
                charS.append(i)
            else:
                if charS:
                    charS.pop()

        for j in T:
            if j != '#':
                charT.append(j)
            else:
                if charT:
                    charT.pop()

        return ''.join(charS) == ''.join(charT)