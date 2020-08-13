# Solution A
class Solution:
    def rotate(self, nums, k):
        i = 0
        while i < k:
            tmp = nums[-1]
            nums[1:] = nums[:-1]
            nums[0] = tmp
            i += 1
        return nums


# Solution B
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def reverse(nums, t, s):
            while t < s:
                nums[t], nums[s] = nums[s], nums[t]
                t += 1
                s -= 1

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)


# Solution C
class Solution:
    def rotate(self, nums, k):
        count, idx, tmp = 0, 0, nums[0]
        done_idx = [0]
        while count < len(nums):
            count, target = count + 1, (idx + k) % len(nums)
            tmp, nums[target] = nums[target], tmp
            if target not in done_idx:
                idx = target
            elif target + 1 < len(nums):
                idx, tmp = target + 1, nums[target + 1]
            done_idx.append(idx)
