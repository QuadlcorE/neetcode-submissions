class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Do we regard each number? 
        # It's a tree question, and we make a decision to either add the current number or not. 
        # when do we back track is when the sum is greater than target. 
        # we could also keep tabs on diff as well, but that's a much bigger set to keep in memory. 
        # we would have to keep a dict of all arrays that might sum up to the dif.
        # lets just stick with the method of a tree adding a value to both sides. 
        solution = []

        def search(solution, nums, i, curr, sum_so_far, target):
            # print("Curr: ", curr, " the sum: ", sum_so_far)
            # Base conditions check
            if sum_so_far == target:
                solution.append(curr.copy())
                return
            if sum_so_far > target:
                return
            # Out of index check 
            if i >= len(nums):
                return

            # Now calculating the new combination
            new_sum_so_far = sum_so_far + nums[i]
            curr.append(nums[i])
            
            # now making the new calls one with i and the other with i+1
            search(solution, nums, i, curr, new_sum_so_far, target)
            curr.pop()
            search(solution, nums, i+1, curr, sum_so_far, target)

            return
        
        search(solution, nums, 0, [], 0, target)
        return solution