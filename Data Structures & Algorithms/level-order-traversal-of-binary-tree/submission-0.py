# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # To do level order traversal of a tree we need to do bfs
        # simply queue and have sublists for each level
        # To know which level a node belongs to we need to append two values to the queue
        # A tuple containing curr level and node
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        res = []
        while q:
            curr = q.popleft()
            node = curr[0]
            lvl = curr[1]

            # We need to add curr to res
            if len(res) == lvl:
                res.append([])
            res[lvl].append(node.val)

            # Then we add the children to it.
            if node.left:
                q.append((node.left, lvl +1))
            if node.right:
                q.append((node.right, lvl +1))
        return res