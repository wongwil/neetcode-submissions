# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)

            if not kth:
                break

              
            groupNext = kth.next

            # reverse between (groupPrev, groupNext)
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # groupPrev has to point to kth now
            # the old pointer of groupPrev becomes the new 
            # groupPrev
            newGroupPrevTmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = newGroupPrevTmp



        return dummy.next
        

    def getKth(self, node, k):
        while k and node:
            node = node.next
            k -= 1

        return node