# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(minheap, (node.val, i, node))
            
        dummy = ListNode()
        curr = dummy
        while minheap:
            val, i, node = heapq.heappop(minheap)
            newnode = ListNode(val)

            curr.next = newnode
            curr = curr.next

            rightnode = node.next
            if rightnode:
                heapq.heappush(minheap, (rightnode.val, i, rightnode))

        return dummy.next
