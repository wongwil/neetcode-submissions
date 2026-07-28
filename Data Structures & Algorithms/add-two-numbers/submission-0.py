# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        
        carry = 0

        curr = dummy
        while l1 or l2 or carry:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val

            res = v1 + v2 + carry

            num = res % 10
            carry = res //  10
            curr.next = ListNode(num)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None



        return dummy.next


