class Solution:
    def merge(self, nums1, m, nums2, n):
        i=m-1
        j=n-1
        tmp=m+n-1
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[tmp]=nums2[j]
                tmp-=1
                j-=1
            else:
                nums1[tmp]=nums1[i]
                tmp-=1
                i-=1
        while j>=0:
            nums1[tmp]=nums2[j]
            tmp-=1
            j-=1