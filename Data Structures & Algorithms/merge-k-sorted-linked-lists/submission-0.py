# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        minlistnode = -1

        while True:
            minlistnode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue

                if minlistnode == -1 or lists[i].val < lists[minlistnode].val:
                    minlistnode = i

            if minlistnode == -1:
                break

            newNode = ListNode(lists[minlistnode].val)
            curr.next = newNode
            curr = newNode

            lists[minlistnode] = lists[minlistnode].next

        return dummy.next
        
            
