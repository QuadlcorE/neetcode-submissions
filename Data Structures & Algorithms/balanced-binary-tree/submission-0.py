# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # To check if a tree is balanced compare the height of the left tree against the right tree. 
        # Question is if a node is found that is unbalanced we return False.
        # Question is how do we know go through all the nodes checking their height and returning their balance factor. 

        def getHeight(node):
            # we just need to return a tuple of height and balance status
            if not node:
                return (0, True)
            ln, rn = getHeight(node.left), getHeight(node.right)
            balance_factor = abs(ln[0] - rn[0])
            maxH = max(ln[0], rn[0])
            if balance_factor > 1:
                return (maxH + 1, False)
            return (maxH + 1, ln[1] and rn[1])
        
        nod = getHeight(root)
        return nod[1]