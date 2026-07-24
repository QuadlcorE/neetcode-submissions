class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # it's a tree kind of thing.
        # We basically add a value or remove a value to the solution set.

        solution = []

        def solve(solution, nums, curr, i):
            # we want to remove a value from rem_nums and solve the remaining nums
            # we also want to add a value from rem_nums before removing it.
            # Base case if rem_nums len is 0 we append to solution
            if i >=len(nums):
                solution.append(curr.copy())
                return 
            
            # which do we do first? 
            # Do we add the value to curr? 
            solve(solution, nums, curr, i+1)
            curr.append(nums[i])
            solve(solution, nums, curr, i+1)
            curr.pop()
            return 
        
        empty = []
        solve(solution, nums, empty, 0)
        return solution
