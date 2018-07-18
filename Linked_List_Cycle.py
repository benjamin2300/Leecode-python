# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head == None or head.next == None:
            return False
        
        visitedMap = {}
        s = head
        while s:
            if s in visitedMap:
                return True
            else:
                visitedMap[s] = True
            s = s.next
        return False
            
            