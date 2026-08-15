class TreeNode:
    def __init__(self, val):
        self.val = val
        self.neighbour = []

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # construct the tree, takes O(n) to create the nodes 0 - n-1
        # We simply store the edge in both. 
        # joining the edges of the tree takes takes O( len(edges) )
        # We then perform a dfs checking if nodes have been visited for all nodes in range 0 - n-1
        # Mind you we have to keep into consideration we might not be given nodes at all ( " is no input a valid input? ")
        # We also have to consider all nodes might not be connected. 
        # To circumvent this we use an explored set so we can keep track of all explored nodes and then cycle through all nodes. 
        # When doing the dfs check we would just keep a curr path and not check the previous node in neighbours

        # Also disconected nodes are considered to not be a tree 
        

        nodes = {}
        for i in range(n):
            nodes[i] = TreeNode(i)
        
        for edge in edges:
            n1 = nodes[edge[0]]
            n2 = nodes[edge[1]]

            n1.neighbour.append(n2)
            n2.neighbour.append(n1)
        
        currpath = set() # we could store the node objects but considering the nodes are identified by val we can just store their val to save space.
        # remember in order to check unconnected nodes we have to use explored
        explored = set() # also use no here

        def dfs(node, prev):
            # First we have to check if we are in a cycle 
            print(currpath, " ", node.val)
            if node.val in currpath:
                return False
            # we add ourselves to the currpath
            currpath.add(node.val)
            explored.add(node.val)

            # cycle through neighbours
            for nei in node.neighbour:
                if prev and nei == prev:
                    continue
                if not dfs(nei, node):
                    print("here?")
                    return False

            currpath.remove(node.val) 
            return True
        
        if not dfs(nodes[0], None):
            return False

        for i in range(n):
            if i not in explored:
                return False
        
        return True
