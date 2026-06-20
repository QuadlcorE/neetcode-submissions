"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # We can store the randoms in a list 
        # Here it should be easier to know which node is being pointed to
        # Are the values unique?
        # If they are we can simply store the values => copy node in a hash map
        # if the values are unique we can simply just use the copy node like I said
        # How about we copy the next nodes rather than the curr node?
        # Are we ever going to have a null list passed into this function?
        # the values are not unique!
        if head == None:
            return None
        copy_map = {}
        curr = head 
        prev = None
        while curr:
           new_copy = Node(curr.val)
           copy_map[curr] = new_copy
           if prev:
            prev.next = new_copy
           prev = new_copy
           curr = curr.next
        
        # We have mapped the nodes now lets add in the randoms
        curr = head
        copy_curr = copy_map[curr]
        while curr:
            if curr.random:
                copy_curr.random = copy_map[curr.random]
            copy_curr = copy_curr.next
            curr = curr.next
        
        return copy_map[head]