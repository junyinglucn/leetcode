# Solution A
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if i == len(nums) - 1 and nums[i - 1] == nums[i]:
                continue
            elif i != len(nums) - 1 and (nums[i - 1] == nums[i] or nums[i + 1] == nums[i]):
                continue
            else:
                return nums[i]
        return nums[0]


# Solution B
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
