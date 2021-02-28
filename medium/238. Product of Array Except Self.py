# Solution A
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, outputs = [0] * n, [0] * n, [0] * n
        l[0], r[n - 1] = 1, 1
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        for i in range(n):
            outputs[i] = l[i] * r[i]

        return outputs


# Solution B
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        outputs = [0] * n
        outputs[0] = 1
        for i in range(1, n):
            outputs[i] = outputs[i - 1] * nums[i - 1]
        r = 1
        for i in range(n - 1, -1, -1):
            outputs[i] = outputs[i] * r
            r *= nums[i]

        return outputs
