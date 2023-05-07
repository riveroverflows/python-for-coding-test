# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left = self.max_depth(root.left)
        right = self.max_depth(root.right)

        return max(left, right) + 1


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

tree2 = TreeNode(1)
tree2.right = TreeNode(2)

s = Solution()
print(s.max_depth(tree))
print(s.max_depth(tree2))
