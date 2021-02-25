# Solution A
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        queue = deque()
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].append(cur)
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adj[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses
