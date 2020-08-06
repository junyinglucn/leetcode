# Solution A
class Solution:
    def maxSubArray(self, nums):
        tmp = nums[0]
        max_ = tmp
        for i in range(1, len(nums)):
            if tmp + nums[i] > nums[i]:
                max_ = max(max_, tmp + nums[i])
                tmp = tmp + nums[i]
            else:
                max_ = max(max_, nums[i], tmp, tmp + nums[i])
                tmp = nums[i]
        return max_


# Solution B
class Solution:
    def maxSubArray(self, nums):
        tmp = nums[0]
        max_ = nums[0]
        for i in nums[1:]:
            tmp = max(tmp + i, i)
            max_ = max(tmp, max_)
        return max_


# Solution C
class Solution:
    def maxSubArray(self, nums):
        cur_sum = 0
        res = nums[0]
        for i in range(len(nums)):
            if cur_sum > 0:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            res = max(res, cur_sum)
        return res


# Solution D
class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            l = self.maxSubArray(nums[0:len(nums) // 2])
            r = self.maxSubArray(nums[len(nums) // 2:len(nums)])
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        return max(l, r, max_l + max_r)
