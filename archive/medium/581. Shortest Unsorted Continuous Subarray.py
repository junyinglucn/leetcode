class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        Max = nums[0]
        r = 0
        for i in range(1, n):
            if nums[i] >= Max:
                Max = nums[i]
            else:
                r = i
        l = n
        Min = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] <= Min:
                Min = nums[i]
            else:
                l = i

        return r - l + 1 if (r - l + 1) > 0 else 0
