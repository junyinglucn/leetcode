# Solution A
class Solution:
    def searchInsert(self, nums, target):
        i = 0
        for j in range(len(nums)):
            if nums[j] == target:
                return j
            elif nums[j] < target:
                i += 1
            elif nums[j] > target:
                break
        return i


# Solution B
class Solution:
    def searchInsert(self, nums, target):
        if target > nums[-1]: return len(nums)
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            else:
                r = m
        return l
