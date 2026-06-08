# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        def remove(curr):
            cnt = 0
            if curr.next:
                cnt = remove(curr.next)
            if cnt == n:
                curr.next = curr.next.next
            return cnt + 1
        
        tmp = ListNode(0, head)
        remove(tmp)
        return tmp.next