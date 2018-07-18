class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegrees = [0] * numCourses
        
        for p in prerequisites:
            indegrees[p[0]] += 1
        
        q = []
        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                q.append(i)
        count = 0
        while len(q) != 0:
            qq = q.pop(0)
            count += 1
            for p in prerequisites:
                if p[1] == qq:
                    indegrees[p[0]] -= 1
                    if indegrees[p[0]] == 0:
                        q.append(p[0])
        if count == numCourses:
            return True
        else:
            return False