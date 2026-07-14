class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        

        def dfs(r,c):
            if (r < 0 or r== rows or c<0 or c == cols or grid[r][c]== 0):
                return 0
            
            grid[r][c] = 0
            
            size = 1
            for direction in directions:
                new_r, new_c = r + direction[0], c+ direction[1]
                size += dfs(new_r,new_c)
            return size
        


        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r,c))
        return area