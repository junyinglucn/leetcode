# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        ct = self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return ct

    def dfs(self, node, path):
        if not node:
            return 0
        path -= node.val
        if path == 0:
            ct = 1 + self.dfs(node.left, path) + self.dfs(node.right, path)
        else:
            ct = 0 + self.dfs(node.left, path) + self.dfs(node.right, path)
        return ct
