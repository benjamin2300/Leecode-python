# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val > l2.val:
            rl = l2
            l2 = l2.next
        else:
            rl = l1
            l1 = l1.next
        start = rl
        
        while True:
            if l1 == None:
                rl.next = l2
                break
            elif l2 == None:
                rl.next = l1
                break
            if l1.val > l2.val:
                rl.next = l2
                l2 = l2.next
            else:
                rl.next = l1
                l1 = l1.next
            rl = rl.next
        return start