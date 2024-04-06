# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        nodes = [root]
        res = [[root.val]]
        while True:
            tmp_res = []
            tmp_nodes = []
            for node in nodes:
                if node.left:
                    l = node.left
                    tmp_res.append(l.val)
                    tmp_nodes.append(l)
                if node.right:
                    r = node.right
                    tmp_res.append(r.val)
                    tmp_nodes.append(r)
            if not tmp_res:
                break
            nodes = tmp_nodes
            res.append(tmp_res)
        return res
