# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution A:
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            n = node.val
            if n <= lower or n >= upper:
                return False
            if not func(node.left, lower, n):
                return False
            if not func(node.right, n, upper):
                return False
            return True

        return func(root)


# Solution B:
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
