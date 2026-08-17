class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Are the values unique? ( We can use an adjacency matrix )
        # We simply need to go through all the nodes and connect them. 
        # Have a seen matrix and go through all nodes 0 to n-1 and when you discover one not in the explored set 
        # Call a dfs on it marking each node as explored

        # No way we have to construct the nodes and their adjacency matrix.
        # Edges is not an adjacency matrix so we have to construct it.
        adjMatrix = [[] for x in range(n)]

        for x, y in edges:
            adjMatrix[x].append(y)
            adjMatrix[y].append(x)

        # Doesn't make sense to create nodes.
        explored = set()
        count = 0

        def dfs(val):
            if val in explored:
                return
            explored.add(val)
            
            for nei in adjMatrix[val]:
                dfs(nei)
        
        for x in range(n):
            if x not in explored:
                count +=1
                dfs(x)

        return count
            
