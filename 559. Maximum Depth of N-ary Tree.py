"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution: 
    def maxDepth(self, root: 'Node') -> int:
        print(root.val)
        for child in root.children:
            print("-", child.val)
            
        return 0


s = Solution()
s.maxDepth([1,null,3,2,4,null,5,6])
s.maxDepth([1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14])