# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Can k be greater than the number of nodes in the tree?
        # If it can't then we can simply store all the nodes in ascending order?
        # Is there some restriction on how much space we have?

        lst = []
        # Perform inorder traversal. 
        def updateLst(node, lst):
            if not node:
                return
            updateLst(node.left, lst)
            lst.append(node.val)
            updateLst(node.right, lst)

        updateLst(root, lst)
        return lst[k-1]