import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        h = []
        for key, val in counter.items():
            heapq.heappush(h, (val, key))
            if len(h) > k:
                heapq.heappop(h)
        return [x[1] for x in h]
