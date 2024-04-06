class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        result = ''
        flag = 1
        for i in range(len(str)):
            if i == 0:
                if str[i] not in ['+', '-'] and not str[i].isdigit():
                    return 0
                if str[i] == '-':
                    flag = -1
                elif str[i] == '+':
                    flag = 1
                else:
                    result += str[i]
            elif not str[i].isdigit():
                break
            else:
                result += str[i]
        if result:
            if -2 ** 31 <= int(result) * flag <= 2 ** 31 - 1:
                return int(result) * flag
            elif flag == -1:
                return - 2 ** 31
            else:
                return 2 ** 31 - 1
        else:
            return 0
