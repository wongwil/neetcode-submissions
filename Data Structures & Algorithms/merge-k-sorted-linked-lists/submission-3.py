# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        myheap = []
        for i in range(len(lists)):
            node = lists[i]
            if node:
                heapq.heappush(myheap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while myheap:
            val, i, node = heapq.heappop(myheap)
            newnode = ListNode(val)
            curr.next = newnode

            nextsmallest = node.next
            if nextsmallest:
                heapq.heappush(myheap, (nextsmallest.val, i, nextsmallest))

            curr = curr.next

        return dummy.next