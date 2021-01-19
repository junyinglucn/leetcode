class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        res = '0'
        for i in range(len(num1) - 1, -1, -1):
            add = 0
            cur = ['0'] * (len(num1) - i - 1)
            for j in range(len(num2) - 1, -1, -1):
                product = int(num1[i]) * int(num2[j]) + add
                cur.append(str(product % 10))
                add = product // 10
            if add > 0:
                cur.append(str(add))
            cur = ''.join(cur[::-1])
            res = self.addStrings(res, cur)
        return res

    def addStrings(self, num1, num2):
        add = 0
        res = list()
        i, j = len(num1) - 1, len(num2) - 1
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            tmp = x + y + add
            res.append(str(tmp % 10))
            add = tmp // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])
