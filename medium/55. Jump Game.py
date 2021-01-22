class Solution:
    def canJump(self, nums: List[int]) -> bool:
        longest = 0
        for i in range(len(nums)):
            if i <= longest:
                longest = max(longest, i + nums[i])
            if longest >= (len(nums) - 1):
                return True
        return False
