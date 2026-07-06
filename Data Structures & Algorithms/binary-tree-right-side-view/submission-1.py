# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Basically level order traversal and update keep updating the last value of the level
        # We don't need to keep all values at each level but simply update the values of each level 
        # thus we only store one value per level.

        if not root:
            return []

        q = deque()
        res = []
        q.append((root, 0))

        while q:
            node, lvl = q.popleft()

            # first add/update res
            if len(res) == lvl:
                res.append(node.val)
            else:
                res[lvl] =node.val
            
            # now add it's children.
            if node.left:
                q.append((node.left, lvl+1))
            if node.right:
                q.append((node.right, lvl+1))
        
        return res