class Solution:
    def plusOne(self, digits):
        for i in range((len(digits) - 1), -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                if digits[0] == 0:
                    digits.insert(0, 1)
        return digits