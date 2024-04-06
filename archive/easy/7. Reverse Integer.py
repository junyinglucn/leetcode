# Solution A:
class Solution:
    def reverse(self, x):
        if -10 < x < 10:
            return x
        str_ = str(x)
        if str_[0] != '-':
            str_ = str_[::-1]
            res = int(str_)
        else:
            str_ = str_[:0:-1]
            res = int(str_)
            res = -res
        return res if -2 ** 31 < res < 2 ** 31 - 1 else 0
