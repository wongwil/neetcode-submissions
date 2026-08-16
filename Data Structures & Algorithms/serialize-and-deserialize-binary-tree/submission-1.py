# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        preord = []
        def dfs(node):
            if not node:
                preord.append("N")
                return

            preord.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(preord)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        preord = data.split(",")

        curr_idx = 0

        def dfs():
            nonlocal curr_idx
            curr_val = preord[curr_idx]

            if curr_val == "N":
                curr_idx += 1
                return None

            curr_node = TreeNode(int(curr_val))
            curr_idx += 1

            curr_node.left = dfs()
            curr_node.right = dfs()

            return curr_node

        return dfs()
