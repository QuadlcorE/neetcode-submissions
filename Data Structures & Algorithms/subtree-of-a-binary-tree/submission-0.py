# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # We basically just want to check if the current node is the same.
        # if it is then we want to return the and result of both children nodes.
        # But we have to find a node that is the same as subroot.
        def checkNodes(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return checkNodes(node1.left, node2.left) and checkNodes(node1.right, node2.right)
        
        # Now we go through the whole root tree looking for the head of subroot 
        q = deque()

        q.append(root)
        # q = [1]
        #   = [2, 3]
        #   = [3, 4, 5]
        while q:
            top = q.popleft()
            if top.left:
                q.append(top.left)
            if top.right:
                q.append(top.right)
            if top.val == subRoot.val:
                if checkNodes(top, subRoot):
                    return True
        
        return False