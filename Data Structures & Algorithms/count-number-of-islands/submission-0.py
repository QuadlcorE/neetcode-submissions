class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we need to go through each cell and check if it's a new island.
        # Am I allowed to edit the grid itself? 
        # We could store a duplicate grid then if we're not allowed to edit grid itself.
        # We could also store visited nodes but that's more data stored than storing the grid itself.
        # We could also keep a set of all nodes that we've visited as well as a tuple. 
        HEIGTH = len(grid)
        WIDTH = len(grid[0])

        seen = set()
        
        def search(x, y):
            if x<0 or x>= HEIGTH or y<0 or y>= WIDTH:
                return 
            if grid[x][y] != "1":
                return 
            if (x,y) in seen:
                return 
            
            # search neighbours after adding to seen
            seen.add((x,y))
            search(x+1, y)
            search(x-1, y)
            search(x, y+1)
            search(x, y-1)

            return 
        
        islands = 0
        # now we go through all squares and check if they are 1 and not in seen
        for i in range(HEIGTH):
            for j in range(WIDTH):
                if (i,j) not in seen and grid[i][j] == "1":
                    # Search it.
                    search(i, j)
                    islands += 1
        
        return islands
            