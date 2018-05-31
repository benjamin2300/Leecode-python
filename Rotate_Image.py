class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #print matrix
        # symmetry x=y
        n = len(matrix)
        for i in range(n):
            for j in range(n-i):
                tmp = matrix[n-1-j][n-1-i]
                matrix[n-1-j][n-1-i] = matrix[i][j]
                matrix[i][j] = tmp
                
        #print matrix
        # symmetry X-axis
        for i in range(n/2):
            for j in range(n):
                tmp = matrix[n-1-i][j]
                matrix[n-1-i][j] = matrix[i][j]
                matrix[i][j] = tmp
        print matrix
        #return matrix