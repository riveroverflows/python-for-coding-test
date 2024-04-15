class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val


class Solution:
    def lowest_common_ancestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode"):
        if root is None:
            return None

        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if root == p or root == q:
            return root
        if left and right:
            return root
        return left or right


root = TreeNode(3)
node5 = TreeNode(5)
root.left = node5
node1 = TreeNode(1)
root.right = node1
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
node4 = TreeNode(4)
root.left.right.right = node4

s = Solution()
print(s.lowest_common_ancestor(root=root, p=node5, q=node1))
print(s.lowest_common_ancestor(root=root, p=TreeNode(5), q=TreeNode(4)))
print(s.lowest_common_ancestor(root=root, p=node5, q=node4))
