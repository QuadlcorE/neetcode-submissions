class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Rather than going from square to edge how about we go from edge to square. 
        # So we go from each edge to find all squares reachable and then mark them for both oceans and then find the intersection?
        ROWS, COLS = len(heights), len(heights[0])

        pacific = [[False] * len(heights[0]) for _ in heights]
        atlantic = [[False] * len(heights[0]) for _ in heights]

        direction = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(row, col, grid):
            grid[row][col] = True
            curr = heights[row][col]
            for incy, incx in direction:
                nr, nc = incy+row, incx+col
                # a square is reachable only if it has a higher or equal number to curr square. 
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] >= curr and not grid[nr][nc]:
                    dfs(nr, nc, grid)
        
        for i in range(COLS):
            dfs(0, i, pacific)
        for i in range(ROWS):
            dfs(i, 0, pacific)
        
        for i in range(ROWS):
            dfs(i, COLS-1, atlantic)
        for i in range(COLS):
            dfs(ROWS-1, i, atlantic)
        
        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if pacific[row][col] == True and atlantic[row][col] == True:
                    result.append([row, col])

        return result