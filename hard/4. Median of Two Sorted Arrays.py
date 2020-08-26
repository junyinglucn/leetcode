class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2

        def helper(nums1, nums2, k):
            if (len(nums1) < len(nums2)):
                nums1, nums2 = nums2, nums1
            if (len(nums2) == 0):
                return nums1[k - 1]
            if (k == 1):
                return min(nums1[0], nums2[0])
            t = min(k // 2, len(nums2))
            if (nums1[t - 1] >= nums2[t - 1]):
                return helper(nums1, nums2[t:], k - t)
            else:
                return helper(nums1[t:], nums2, k - t)

        return (helper(nums1, nums2, k1) + helper(nums1, nums2, k2)) / 2
