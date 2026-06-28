# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # I would want to return the depth of the tree
        # Have a max value that I update by adding the depth of the right and left node of each node.
        maxD = 0
        def checkD(node: TreeNode, depth: int) -> int:
            nonlocal maxD
            if not node:
                return depth
            ld = checkD(node.left, depth)
            rd = checkD(node.right, depth)
            
            maxD = max(maxD, ld+rd)
            
            return max(ld+1, rd+1)
        checkD(root, 0)
        return maxD