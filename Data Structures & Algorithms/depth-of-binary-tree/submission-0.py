# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkD(self, root: TreeNode, depth):
        if not root:
            return depth
        depth = max(self.checkD(root.left, depth), self.checkD(root.right, depth))
        return depth + 1
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.checkD(root, 0)
