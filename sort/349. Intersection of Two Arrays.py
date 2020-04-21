# solution A
class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


# solution B
class Solution:
    def intersection(self, nums1, nums2):
        d = {}
        new = []
        for i in nums1:
            if not d.get(i):
                d[i] = 1
        for i in nums2:
            if d.get(i):
                new.append(i)
                d[i] -= 1
        return new


# solution C
class Solution:
    def intersection(self, nums1, nums2):
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        new = []
        if len(nums1) < len(nums2):
            for i in nums1:
                if i in nums2 and i not in new:
                    new.append(i)
        else:
            for i in nums2:
                if i in nums1 and i not in new:
                    new.append(i)
        return new
