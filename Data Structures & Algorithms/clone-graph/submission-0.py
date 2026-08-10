"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Take note node can be null
        if not node:
            return None
        # can two nodes have the same value? 
        # I can store the nodes in sets. 
        # I can use a mapping of values to node
        # So for each node I basically just value I basically just map to it's node copy.
        cpySeen = {}

        # now how do I go through all nodes? 
        # I could use a queue and add a new node unto the queue when I discover it.
        # Do I add the actual node or the clone? I think the actual node
        queue = deque()
        queue.append(node)

        # now while queue we go through each node in the queue
        # For each node in the queue we go through it's neighbours 
        # we append the neighbour if it's value is not in cpySeen and then add their copy to cpySeen
        # for each node we visit we make a copy of it. 
        # if we only make a cpy of neibouring nodes we need to make a cpy of the first node before we start
        
        firstNode = Node(node.val, None)
        cpySeen[node.val] = firstNode

        # Now we go through all the queue
        while queue:
            curr = queue.popleft()
            currCpy = cpySeen[curr.val]
            for nei in curr.neighbors:
                # if not in cpySeen create a new cpy of nei and append it to cpySeen 
                # also append nei to queue
                if nei.val not in cpySeen:
                    queue.append(nei)
                    cpy = Node(nei.val, None)
                    cpySeen[nei.val] = cpy
                
                # Now just update the neighbours list of this curr node
                # use the cpy
                currCpy.neighbors.append(cpySeen[nei.val])
        
        return cpySeen[node.val]
                
