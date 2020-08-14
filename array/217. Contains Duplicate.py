# Solution A
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

# Solution B
class Solution:
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

# Solution C
class Solution:
    def containsDuplicate(self, nums):
