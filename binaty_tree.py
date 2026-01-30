from operator import invert


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        cur = root
        if cur:
            cur.left, cur.right = cur.right, cur.left
            self.invertTree(cur.left)
            self.invertTree(cur.right)
        else:
            return None

        return root

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root.right and root.left:
            return 1
        elif not root.right:
            return self.diameterOfBinaryTree(root.left)
        elif not root.left:
            return self.diameterOfBinaryTree(root.right)
        return self.maxDepth(root.left) + self.maxDepth(root.right)