# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution A
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        sub_path = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        return [str(root.val) + '->' + s for s in sub_path]
