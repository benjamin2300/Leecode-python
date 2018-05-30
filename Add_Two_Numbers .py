# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f = l1
        s = l2
        q = 0
        r = 0
        AR = ListNode(0)
        a = AR
        while f or s:
            
            if not f:
                summ = 0 + s.val + a.val
                s = s.next
            elif not s:
                summ = 0 + f.val + a.val
                f = f.next
            else:
                summ = f.val + s.val + a.val
                f = f.next
                s = s.next         
            r = summ % 10
            a.val = r
            q = summ / 10
            if f or s or q:
                a.next = ListNode(q)
                a = a.next
            
        return AR
                
            