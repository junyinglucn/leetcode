class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pt0 = 0
        pt1 = 0
        for i in range(n):
            if nums[i] == 0:
                nums[pt0], nums[i] = nums[i], nums[pt0]
                if pt0 < pt1:
                    nums[pt1], nums[i] = nums[i], nums[pt1]
                pt0 += 1
                pt1 += 1
            elif nums[i] == 1:
                nums[pt1], nums[i] = nums[i], nums[pt1]
                pt1 += 1
