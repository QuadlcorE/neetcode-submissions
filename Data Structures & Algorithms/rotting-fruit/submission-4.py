class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # go through keeping track of good fruits 
        # create a queue adding bad fruits 
        # For each fruit in queue we rot adjacent fruits using bfs

        queue = deque()
        goodFruits = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    goodFruits += 1
                if grid[row][col] == 2:
                    queue.append(((row, col), 0))

        time = 0
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            # append new fruits and rot them 
            curr = queue.popleft()
            row, col = curr[0]
            time = curr[1]
            for incy, incx in direction:
                if row+incy in range(len(grid)) and col+incx in range(len(grid[0])) and grid[row+incy][col+incx] == 1:
                    queue.append(((row+incy, col+incx), curr[1]+1))
                    grid[row+incy][col+incx] = 2
                    goodFruits -= 1

        if goodFruits > 0:
            return -1

        return time