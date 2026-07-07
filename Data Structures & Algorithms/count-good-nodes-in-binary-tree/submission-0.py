# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # We only have to check this nodes children
        # And return the count
        # Are we considering the parents parent?
        # like if root was 5 and we had 2=> 4 then are both nodes bad?
        # if that's the case we just need to pass in the max value seen
        # Basically it's a min tree. And we are verifying how many nodes abide by that

        def dfs(maxSeen, node):
            cnt = 0
            if not node:
                return cnt
            
            if maxSeen <= node.val:
                cnt +=1
            
            return cnt + dfs(max(maxSeen, node.val), node.left) + dfs(max(maxSeen, node.val), node.right)
        
        maxSeen = float("-inf")
        cnt = dfs(maxSeen, root)
        return cnt