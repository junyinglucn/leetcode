class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.minheap = []

        for i in range(min(k, len(nums))):
            self.minheap.append(nums[i])
            self.sift_up(i)

        for num in nums[k:]:
            if num > self.minheap[0]:
                self.minheap[0] = num
                self.sift_down(0, k - 1)

    def sift_up(self, new_idx):
        new_val = self.minheap[new_idx]
        while new_idx > 0 and new_val < self.minheap[(new_idx - 1) // 2]:
            self.minheap[new_idx] = self.minheap[(new_idx - 1) // 2]
            new_idx = (new_idx - 1) // 2
        self.minheap[new_idx] = new_val

    def sift_down(self, start, end):
        start_val = self.minheap[start]
        while start * 2 + 1 <= end:
            child = start * 2 + 1
            if child + 1 <= end and self.minheap[child] > self.minheap[child + 1]:
                child += 1
            if start_val > self.minheap[child]:
                self.minheap[start] = self.minheap[child]
                start = child
            else:
                break
        self.minheap[start] = start_val

    def add(self, val):
        if len(self.minheap) < self.k:
            self.minheap.append(val)
            self.sift_up(len(self.minheap) - 1)
        elif self.minheap[0] < val:
            self.minheap[0] = val
            self.sift_down(0, self.k - 1)
        return self.minheap[0]
