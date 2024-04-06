# Solution A
class Solution:
    def majorityElement(self, nums):
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for key in d.keys():
            if d[key] > (len(nums) / 2):
                return key


# Solution B
class Solution:
    def majorityElement(self, nums):
        cur = nums[0]
        count = 0
        for i in nums:
            if cur == i:
                count += 1
            else:
                count -= 1
                if count == 0:
                    cur = i
                    count = 1
        return cur
