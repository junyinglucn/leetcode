# solution A
class Solution:
    def minSubsequence(self, nums):
        s=sorted(nums,reverse=True)
        for i in range(len(s)+1):
            sub=s[:i]
            left=s[i:]
            if sum(sub)>sum(left):
                break
        return sub

# solution B
class Solution:
    def minSubsequence(self, nums):
        nums.sort(reverse=True)
        total = sum(nums)
        tmp = 0
        for i, ii in enumerate(nums):
            tmp += ii
            if 2*tmp > total:
                return nums[0:i+1]