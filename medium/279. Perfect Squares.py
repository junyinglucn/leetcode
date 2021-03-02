# Solution A
class Solution:
    def numSquares(self, n: int) -> int:
        lst = [i * i for i in range(1, n) if i * i <= n]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            min_n = i
            for j in [c for c in lst if c <= i]:
                if dp[i - j] + 1 < min_n:
                    min_n = dp[i - j] + 1
            dp[i] = min_n
        return dp[n]


# Solution B
class Solution:
    def numSquares(self, n: int) -> int:
        from collections import deque
        if n == 0:
            return 0
        queue = deque([n])
        step = 0
        visited = set()
        while queue:
            step += 1
            for _ in range(len(queue)):
                tmp = queue.pop()
                for i in range(1, int(tmp ** 0.5) + 1):
                    res = tmp - i ** 2
                    if res == 0:
                        return step
                    if res not in visited:
                        queue.appendleft(res)
                        visited.add(res)
        return step
