
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue  = deque()
        fresh = 0
        time = 0

        rows = len(grid)
        cols = len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1 
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue and fresh >0 :
            length = len(queue)
            for r in range(length):
                r,c = queue.popleft()

                for direction in directions:
                    row, col = r+direction[0], c+ direction[1]

                    if (row in range(rows) and col in range(cols) and grid[row][col]==1):
                        grid[row][col] = 2
                        queue.append((row,col))
                        fresh -=1
            time+=1
        return time if fresh== 0 else -1

