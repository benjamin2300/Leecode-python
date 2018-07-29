"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        eMap = {}
        for e in employees:
            eMap[e.id] = e
        q = [id]
        summon = 0
        while q:
            e = eMap[q.pop()]
            summon += e.importance
            for s in e.subordinates:
                q.append(s)
        return summon