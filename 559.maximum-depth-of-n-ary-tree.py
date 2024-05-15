#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, node) -> int:
        
        if not node: return 0

        # if no children return 1
        if len(node.children) < 1: return 1

        # if a node has children, you return depth of max child depth + 1"
        maxdepth = 0
        for child in node.children:
            maxdepth = max(maxdepth, self.maxDepth(child))

        return maxdepth + 1


# @lc code=end