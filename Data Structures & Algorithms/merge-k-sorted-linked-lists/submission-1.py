# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Simple solution is to keep merging each list to the result list
        merged_list = ListNode()
        for each in lists:
            curr = merged_list.next
            iterator = each
            prev = merged_list
            while iterator:
                if curr and curr.val <= iterator.val:
                    prev = curr
                    curr = curr.next
                else:
                    prev.next = iterator
                    prev = prev.next
                    tmp = iterator.next
                    iterator.next = curr
                    iterator = tmp
        return merged_list.next