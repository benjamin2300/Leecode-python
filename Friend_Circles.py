
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = []
        N = len(M)
        count = 0
        for i in range(N):
            if i not in visited:
                count+=1
                self.dfs(i, visited, M)
        return count
    def dfs(self, x, visited, M):
        for i in range(len(M)):
            if M[x][i] == 1 and i not in visited:
                visited.append(i)
                self.dfs(i, visited, M)