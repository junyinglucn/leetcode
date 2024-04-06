class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                nums[(i + 1):] = sorted(nums[(i + 1):])
                for j in range(i + 1, n):
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                return nums
        return nums.sort()
