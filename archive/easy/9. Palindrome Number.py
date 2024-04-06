# Solution A
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x[::-1] == x:
            return True
        return False

# Solution B
class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rem = 0
        while x > rem:
            rem = rem * 10 + x % 10
            x = x // 10
        return x == rem or x == rem // 10
