class Solution:
    def thirdMax(self, nums):
        first = float('-inf')
        second = float('-inf')
        third = float('-inf')
        for num in nums:
            if num > third:
                if num < second:
                    third = num
                elif num > second:
                    if num < first:
                        third = second
                        second = num
                    elif num > first:
                        third = second
                        second = first
                        first = num
        if third == float('-inf'):
            return first
        else:
            return third
