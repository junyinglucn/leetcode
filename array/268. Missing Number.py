# Solution A
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                return i + 1
