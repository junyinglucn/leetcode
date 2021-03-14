# Solution A
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        mp = {}

        def dfs(i, cursum):
            if i == n:
                return 0 if cursum != S else 1

            if (i, cursum) not in mp:
                mp[(i, cursum)] = dfs(i + 1, cursum - nums[i]) + dfs(i + 1, cursum + nums[i])

            return mp[(i, cursum)]

        return dfs(0, 0)


# Solution B
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        dp = {(0, 0): 1}
        for i in range(1, n + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((n, S), 0)
