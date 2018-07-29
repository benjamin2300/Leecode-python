# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.map = {}
        return self.search(root, k)
    def search(self, node, k):
        if node != None:
           
            for key in self.map:
                if self.map[key] == node.val:
                    return True
            if node.val not in self.map:
                self.map[node.val] = k - node.val
            
            if self.search(node.left, k):
                return True
            if self.search(node.right, k):
                return True
            return False