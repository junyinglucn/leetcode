# Solution A
class Solution:
    def moveZeroes(self, nums):
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i] = nums[j]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0


# Solution B
class Solution:
    def moveZeroes(self, nums):
        if not nums:
            return 0
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
