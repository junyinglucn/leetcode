class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        d = {0: 1}
        total = 0
        for n in nums:
            total += n
            res += d.get((total - k), 0)
            d[total] = d.get(total, 0) + 1
        return res
