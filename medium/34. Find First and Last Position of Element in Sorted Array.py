class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        l2 = left
        r2 = len(nums) - 1
        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if nums[m2] == target:
                l2 = m2 + 1
            elif nums[m2] > target:
                r2 = m2 - 1
        return [left, l2 - 1]
