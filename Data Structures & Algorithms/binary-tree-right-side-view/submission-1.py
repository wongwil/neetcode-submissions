# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        
        q = deque([root])
        res = []
        while q:
            qLen = len(q)

            lastnode = None
            for i in range(qLen):
                lastnode = q.popleft()

                if lastnode.left:
                    q.append(lastnode.left)

                if lastnode.right:
                    q.append(lastnode.right)
            
            res.append(lastnode.val)

        return res

