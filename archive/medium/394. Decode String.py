class Solution:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], '', 0
        for c in s:
            if '0' <= c <= '9':
                multi = multi * 10 + int(c)
            elif c == '[':
                stack.append([res, multi])
                res, multi = '', 0
            elif c == ']':
                last_res, cur_multi = stack.pop()
                res = last_res + cur_multi * res
            else:
                res += c
        return res
