# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.level_map = {}
        level = self.levelSearch(root, 0)
        avg = []
        for key in self.level_map:
            avg.append(mean(self.level_map[key]))
        return avg
        
    def levelSearch(self, node, level):
        if node == None:
            return level
        if level not in self.level_map:
            self.level_map[level] = []
            
        self.level_map[level].append(node.val)
        self.levelSearch(node.left, level+1)
        self.levelSearch(node.right, level+1)

def mean(nums):
    return float(sum(nums)) / len(nums)