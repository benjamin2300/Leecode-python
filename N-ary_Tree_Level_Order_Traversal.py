"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res =[]
        res = self.levelSearch(root, 0, res)
        return res
    
    def levelSearch(self, node, level, res):
        if node != None:
            if level >= len(res):
                res.append([])
                
            res[level].append(node.val)
            for ch in node.children:
                res =self.levelSearch(ch, level+1, res)
        return res