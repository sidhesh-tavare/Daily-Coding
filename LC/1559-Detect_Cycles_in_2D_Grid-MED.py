class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        visited = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        row,col = len(grid),len(grid[0])
        
        def dfs(r,c,pr,pc,char):
            visited.add((r,c))
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if nr in range(row) and nc in range(col) and (nr,nc)!=(pr,pc):
                    if grid[nr][nc] == char:
                        if (nr,nc) in visited: return True 
                        if dfs(nr,nc,r,c,char): return True 

        for r in range(row):
            for c in range(col):
                if (r,c) not in visited:
                    if dfs(r,c,-1,-1,grid[r][c]): return True 

        return False
    
# not optimised :)
# URL : https://leetcode.com/problems/detect-cycles-in-2d-grid/description/?envType=daily-question&envId=2026-04-26