class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maximum = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[0]*n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                maximum = max(maximum, self.search(grid, i, j, 0, visited))        
        return maximum
                
    def search(self, grid, i, j, count, visited):
        
        m = len(grid)
        n = len(grid[0])
        if grid[i][j] == 0:
            return count
        if visited[i][j] == 0:
            count += 1
            visited[i][j] = 1
            for w in [-1, 1]:
                if  i+w >=0 and i+w < m:
                    if visited[i+w][j] == 0:
                        count = max(count, self.search(grid, i+w, j, count, visited))
            for h in [-1, 1]:
                if j+h >= 0 and j+h <n:
                    if visited[i][j+h] == 0:
                        count = max(count, self.search(grid, i, j+h, count, visited))
        return count