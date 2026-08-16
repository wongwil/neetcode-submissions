# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder tells me the next root elements but i don't know if they belong
        # to the right or left subtree

        # inorder tells me the split of the left and right subtrees.

        # i keep track of inorder subarrays and call it recursively
        # while moving on to the next element in preorder at each call
        
        # we use a map for inorder to get O(1) access to the subroot element
        # instead of slicing the inorder subarrays, we keep track of l and r indeces
        # for O(1) memory

        inorder_map = {val:i for i, val in enumerate(inorder)}
        self.subroot_idx = 0

        def dfs(l,r):
            if r < l:
                return None

            subroot_val = preorder[self.subroot_idx]
            mid = inorder_map[subroot_val]

            subroot = TreeNode(subroot_val)
            self.subroot_idx += 1

            subroot.left = dfs(l, mid - 1)
            subroot.right = dfs(mid + 1, r)

            return subroot

        return dfs(0, len(preorder) - 1)