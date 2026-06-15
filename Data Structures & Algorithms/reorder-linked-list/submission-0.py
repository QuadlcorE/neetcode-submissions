# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fp = head
        sp = head

        while fp and fp.next:
            fp = fp.next.next
            sp = sp.next
        
        second_half = sp.next
        prev = sp.next = None

        while second_half:
            tmp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = tmp
        
        curr = head
        second_half = prev
        while second_half:
            tmp1, tmp2 = curr.next, second_half.next
            curr.next = second_half
            second_half.next = tmp1
            curr, second_half = tmp1, tmp2
           
