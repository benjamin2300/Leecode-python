# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)
        
    def dfs(self, node, depth):
        if node != None:
            d1 = self.dfs(node.left, depth+1)
            d2 = self.dfs(node.right, depth+1)
            return max(d1, d2)
        else:
            return depth
            