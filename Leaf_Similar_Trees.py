# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        l1 = []
        l2 = []
        
        l1 = self.get_leaf(root1, l1)
        l2 = self.get_leaf(root2, l2)
        if l1 == l2:
            return True
        else:
            return False
        
        
        
    def get_leaf(self, node, l):
        if node != None:
            if node.left == None and node.right == None:
                l.append(node.val)
                return l
            l = self.get_leaf(node.left, l)
            l = self.get_leaf(node.right, l)
        return l