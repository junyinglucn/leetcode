# Solution A
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]


# Solution B
class Solution:
    def maxHeapify(self, a, i, heapSize):
        l = i * 2 + 1
        r = i * 2 + 2
        largest = i
        if l < heapSize and a[l] > a[largest]:
            largest = l
        if r < heapSize and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            self.maxHeapify(a, largest, heapSize)

    def buildMaxHeap(self, a, heapSize):
        for i in range(heapSize // 2, -1, -1):
            self.maxHeapify(a, i, heapSize)

    def findKthLargest(self, nums, k):
        heapSize = len(nums)
        self.buildMaxHeap(nums, heapSize)
        for i in range(len(nums) - 1, len(nums) - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapSize -= 1
            self.maxHeapify(nums, 0, heapSize)
        return nums[0]
