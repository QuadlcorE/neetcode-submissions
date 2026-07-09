# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # when searching the left subtree we update the maxnode 
        # when searching the right subtree we update the minnode
        def verify(node, highest, lowest):
            if not node:
                return True
            if node.val >= highest or node.val <= lowest:
                return False
            return verify(node.left, node.val, lowest) and verify(node.right, highest, node.val)
        
        return verify(root, float("inf"), float("-inf"))