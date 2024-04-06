# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution A
class Solution:
    def inorderTraversal(self, root):
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = []
        inorder(root)
        return res


# Solution B
class Solution:
    def inorderTraversal(self, root):
        white, gery = 0, 1
        res = []
        stack = [(white, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == white:
                stack.append((white, node.right))
                stack.append((gery, node))
                stack.append((white, node.left))
            else:
                res.append(node.val)
        return res
