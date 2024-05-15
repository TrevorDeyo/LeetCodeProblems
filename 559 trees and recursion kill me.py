
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

    def addChild(self, child):
        self.children.append(child)


class Solution:
    def maxDepth(self, node) -> int:
        # if a node has no children, you return a depth of 1
        if len(node.children) < 1: return 1

        # if a node has children, you return depth of max child depth + 1"
        maxdepth = 0
        for child in node.children:
            maxdepth = max(maxdepth, self.maxDepth(child))

        return maxdepth + 1


# [1,null,3,2,4,null,5,6]
three = Node(3)
three.addChild(Node(5))
three.addChild(Node(6))

root = Node(1)
root.addChild(three)
root.addChild(Node(2))
root.addChild(Node(4))

solution = Solution()

print(solution.maxDepth(root)) # 3