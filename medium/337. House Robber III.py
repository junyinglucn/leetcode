# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        a = self.helper(root)
        return max(a[0], a[1])

    def helper(self, root):
        if not root:
            return [0, 0]
        l = self.helper(root.left)
        r = self.helper(root.right)
        v1 = l[1] + r[1] + root.val
        v2 = max(l[0], l[1]) + max(r[0], r[1])
        return [v1, v2]
