# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxseen):
            res = 0
            if not node:
                return res

            if node.val >= maxseen:
                res += 1

            res += dfs(node.left, max(maxseen, node.val))
            res += dfs(node.right, max(maxseen, node.val))

            return res

        return dfs(root, root.val)