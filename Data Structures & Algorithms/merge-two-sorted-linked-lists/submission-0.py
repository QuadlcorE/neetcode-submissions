# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0, None)
        ptr1 = list1
        ptr2 = list2
        curr = newHead
        while ptr1 or ptr2:
            if ptr1 and ptr2:
                if ptr1.val <= ptr2.val:
                    curr.next = ptr1
                    ptr1 = ptr1.next
                else:
                    curr.next = ptr2
                    ptr2 = ptr2.next
            elif ptr1:
                curr.next = ptr1
                break
            else:
                curr.next = ptr2
                break
            curr = curr.next
        return newHead.next
        