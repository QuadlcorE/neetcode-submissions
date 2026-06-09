# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        top = l1 
        bottom = l2
        carry = 0
        result = ListNode(0, None)
        curr = result
        while top or bottom or carry > 0:
            curr.next = ListNode(0, None)
            curr = curr.next
            summ = 0
            if top:
                summ += top.val
                top = top.next
            if bottom:
                summ += bottom.val
                bottom = bottom.next
            summ += carry 
            curr.val = summ % 10
            carry = summ//10
            
        return result.next