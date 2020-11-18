class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 3:
            return nums[0] + nums[1] + nums[2]
        d = float('inf')
        nums.sort()
        res = 0
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r] - target
                if abs(tmp) < d:
                    d = abs(tmp)
                    res = nums[i] + nums[l] + nums[r]
                elif tmp > 0:
                    r -= 1
                elif tmp < 0:
                    l += 1
                else:
                    return target
        return res
