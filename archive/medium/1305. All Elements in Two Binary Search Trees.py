# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, path):
        if root is None:
            return
        self.dfs(root.left, path)
        path.append(root.val)
        self.dfs(root.right, path)

    def getAllElements(self, root1, root2):
        l1 = []
        l2 = []
        self.dfs(root1, l1)
        self.dfs(root2, l2)

        i, j = 0, 0
        out = []
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                out.append(l1[i])
                i += 1
            else:
                out.append(l2[j])
                j += 1

        if i < len(l1):
            out.extend(l1[i:])
        if j < len(l2):
            out.extend(l2[j:])

        return out
