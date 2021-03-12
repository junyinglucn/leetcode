# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        prefix_sum = collections.defaultdict(int)
        prefix_sum[0] = 1
        pre = 0
        ans = 0

        def preOrder(root):
            nonlocal pre, prefix_sum, sum, ans
            if not root:
                return
            pre += root.val
            ans += prefix_sum[pre - sum]
            prefix_sum[pre] += 1

            preOrder(root.left)
            preOrder(root.right)

            prefix_sum[pre] -= 1
            pre -= root.val

        preOrder(root)
        return ans
