# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level_map = {}
        level_map = self.levelSearch(root, 0, level_map)
        depth = len(level_map)
        rlist = []
        for i in range(depth):
            l = []
            for val in level_map[depth-1-i]:
                l.append(val)
            rlist.append(l)
        return rlist
    def levelSearch(self, node, level, level_map):
        if node == None:
            return level_map
        else:
            if level in level_map:
                l = level_map[level]
                l.append(node.val)
            else:
                level_map[level] = [node.val]
            level_map = self.levelSearch(node.left, level+1, level_map)
            level_map = self.levelSearch(node.right, level+1, level_map)
        return level_map