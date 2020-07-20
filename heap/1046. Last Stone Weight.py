# Solution A
class Solution:
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]


# Solution B
from heapq import heapify,heappush,heappop
class Solution:
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i];
        heapify(stones)
        while len(stones) > 0:
            y = -heappop(stones)
            if len(stones) == 0:
                return y
            x = -heappop(stones)
            if x != y:
                heappush(stones, x - y)
        return 0
