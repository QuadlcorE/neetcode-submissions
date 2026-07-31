class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Can I sort the candidates? 
        # Cause if it's sorted then we don't have to worry about duplicate solutions? Won't solve duplicate solutions
        # if we get [1,1,1,2,3] trying to get target of 3
        # if we've seen one 1 can we say we've covered all the solutions that could have a one? Yes.
        # but then we would have to use a while loop instead of a recursive call to cycle through all numbers? Does that work?
        # we have the solution [[1,1,1],[1,2],[3]]

        solution = []

        def search(i, curr, sum_so_far):
            # Base cases 
            # win condition 
            if sum_so_far == target:
                solution.append(curr.copy())
                return
            if sum_so_far > target:
                return
            
            # out of bounds
            if i >= len(candidates):
                return

            # Searching 
            # we either add ith value or we don't add ith value
            # We can never use the current value more than once. 
            new_sum_so_far = candidates[i] + sum_so_far
            curr.append(candidates[i])
            search(i+1, curr, new_sum_so_far)
            curr.pop()
            # this is where we have an issue 
            # if we made the call on the second 1 we might have the check here where we keep going to the next non similar value. 
            dif = 1
            while i+dif<len(candidates) and candidates[i] == candidates[i+dif]:
                dif +=1
            if dif+i>=len(candidates):
                return
            search(i+dif, curr, sum_so_far)
        
        candidates.sort()
        search(0, [], 0)
        return solution