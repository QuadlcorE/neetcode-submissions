# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowptr = head
        fastptr = head
        while fastptr:
            if not fastptr or not fastptr.next:
                return False
            fastptr = fastptr.next.next
            slowptr = slowptr.next
            if fastptr == slowptr:
                return True
        return False