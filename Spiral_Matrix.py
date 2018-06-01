class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        n = len(matrix)
        if n == 0:
            return []
        m = len(matrix[0])
        hs = 0
        he = m
        vs = 0
        ve = n
        vh = 0
        count = 0
        ans = []

        while count!= m*n:
            if vh % 4 == 0:
                for i in range(hs, he, 1):
                    print matrix[vs][i]
                    ans.append(matrix[vs][i])
                    count+=1
                vs += 1
            elif vh % 4 == 1:
                for i in range(vs, ve, 1):
                    print matrix[i][he-1]
                    ans.append(matrix[i][he-1])
                    count+=1
                he -= 1
            elif vh % 4 == 2:
                s = he
                e = hs
                for i in range(he, hs, -1):
                    print matrix[ve-1][i-1]
                    print he, hs
                    ans.append(matrix[ve-1][i-1])
                    count+=1
                ve -= 1
            elif vh % 4 == 3:
                s = ve
                e = vs
                for i in range(ve, vs, -1):
                    print matrix[i-1][hs]
                    ans.append(matrix[i-1][hs])
                    count+=1
                hs += 1
            print "tt"
            #count+=1
            vh+=1
        return ans
            
 