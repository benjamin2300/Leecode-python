# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        depth =  self.findDepth(root)
        self.width = (1 << depth) - 1
        #create empty array
        self.pbt = [[""]*self.width for i in range(depth)]
       
        self.trace_and_set(root, 1, self.width / 2)
        return self.pbt
        
    def findDepth(self, root):
        if root != None:
            return 1+max(self.findDepth(root.left), self.findDepth(root.right))
        else:
            return 0
    
    def trace_and_set(self, node, depth, position):
        
        if not node:
            return
        print depth, position
        
        self.pbt[depth-1][position] = str(node.val)
        gap = 1 + self.width >> (depth + 1)
        self.trace_and_set(node.left, depth+1, position-gap)
        self.trace_and_set(node.right, depth+1, position+gap)
        
  