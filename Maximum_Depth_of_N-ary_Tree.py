"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """

        return self.get_depth(root, 0)
    
    def get_depth(self, node, depth):
        no_leaf = True

        if node != None:
            depth += 1
            if len(node.children) == 0:
                return depth
            else:
                re = []
                for ch in node.children:
                    re.append(self.get_depth(ch, depth))
                depth = max(re)

        return depth
                