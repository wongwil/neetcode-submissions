"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copymap = defaultdict(lambda:Node(0))
        copymap[None] = None
        curr = head

        while curr:
            copymap[curr].val = curr.val
            copymap[curr].next = copymap[curr.next]
            copymap[curr].random = copymap[curr.random]
            curr = curr.next

        return copymap[head]
