# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        res = self.inOrder(root, res)
        diff = 100000
        
        for i in range(1, len(res)):
            if res[i] - res[i-1] < diff:
                diff = res[i] - res[i-1]
        return diff
    
    def inOrder(self, node, res):
        if node != None:
            res = self.inOrder(node.left, res)
            res.append(node.val)
            res = self.inOrder(node.right, res)
        return res