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


# Solution B
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i, adj, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adj[i]:
                if not dfs(j, adj, flags):
                    return False
            flags[i] = -1
            return True

        adj = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adj, flags):
                return False
        return True
