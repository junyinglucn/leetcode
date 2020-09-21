# Definition for a binary tree node. class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        sum, stack, p = 0, [], root
        while p or stack:
            while p:
                stack.append(p)
                p = p.right
            p = stack.pop()
            sum += p.val
            p.val = sum
            p = p.left
        return root
