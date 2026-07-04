# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If it's a bst all values are sorted to find a common ancestor we just need to find where both values are not in the same subtree. 
        # When we find this we know the LCA then we need to return it.
        # By lowest common ancestor do we mean the smallest ancestor so assuming we have a tree like this
        # Are we always going to have a result?
        # Is p ever going to equate to q?
        if p.val == root.val or q.val == root.val:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor( root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor( root.left, p, q)
        else:
            return root
            