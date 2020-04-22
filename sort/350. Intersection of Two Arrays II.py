class Solution:
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        p1, p2 = 0, 0
        r = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                r.append(nums1[p1])
                p1 += 1
                p2 += 1
        return r
