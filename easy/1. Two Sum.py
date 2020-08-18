class Solution:
    def twosum(self, nums, target):
        hash = {}
        l = len(nums)
        for n in range(l):
            if target - nums[n] in hash:
                return [hash[target - nums[n]], n]
            else:
                hash[nums[n]] = n
