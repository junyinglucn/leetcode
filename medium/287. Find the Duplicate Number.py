# Solution A
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        present = set()
        for i in nums:
            if i in present:
                return i
            else:
                present.add(i)


# Solution B
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1
        while left < right:
            ct = 0
            mid = (left + right) // 2
            for n in nums:
                if n <= mid:
                    ct += 1
            if ct > mid:
                right = mid
            else:
                left = mid + 1
        return right
