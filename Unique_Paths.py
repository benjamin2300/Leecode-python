class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp_map = [[0]*n] * m
        #print dp_map
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    print i, j
                    dp_map[i][j] = 1

                else:
                    dp_map[i][j] = dp_map[i-1][j] + dp_map[i][j-1]
                    #print dp_map[j-1][i], dp_map[j][i-1]
                
                
        return dp_map[m-1][n-1]
        
        