class CourseNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # We need to make sure there is no cycle when we build the tree. 
        # But that means we need to build a tree first.
        # We could go through all nodes in the tree using a visited set and make check their children 
        # Essentially construck a tree using the prerequisites array
        # Create a seen set 
        # Go through all nodes from 0-numCourses-1
        # perform a dfs on each using a set for currPath
        # if the currnode has a pointer to a node we've seen before ( currPath ) we return Fasle in total. 
        # If we go through all nodes then we return true.

        # Handling emptyCourses
        if len(prerequisites) <= 0:
            return True 

        # First create a hash map and fill with all nodes
        nodes = {}
        for i in range(numCourses):
            nodes[i] = CourseNode(i)

        for match in prerequisites:
            course = nodes[match[0]]
            pre = nodes[match[1]]
            # connect them 
            pre.children.append(course)
        
        # now for all courses in the course range
        # Perform dfs if not in explored

        explored = set()
        currPath = set()

        def dfs(node):
            if node in currPath:
                return False
            if node in explored:
                return True

            currPath.add(node)
            explored.add(node)
            for entry in node.children:
                if not dfs(entry):
                    return False
            currPath.remove(node)
            return True
        
        for i in range(numCourses):
            if nodes[i] in explored:
                continue
            if not dfs(nodes[i]):
                return False
        
        return True
            