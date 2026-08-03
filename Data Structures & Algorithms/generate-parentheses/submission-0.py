class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(lN, rN):
            if lN == rN == n:
                result.append("".join(stack))
                return
            
            if lN < n:
                stack.append("(")
                backtrack(lN + 1, rN)
                stack.pop()
            
            if rN < lN:
                stack.append(")")
                backtrack(lN, rN + 1)
                stack.pop()

        backtrack(0, 0)
        return result