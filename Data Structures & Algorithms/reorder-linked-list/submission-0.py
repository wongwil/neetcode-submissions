# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next


        half = slow

        curr = half.next
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp

        right = prev
        half.next = None

        curr = head

        while curr and right:
            templeft = curr.next
            tempright = right.next

            curr.next = right
            right.next = templeft

            right = tempright
            curr = templeft



        