class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # The best way is for every next position we should have a decision using every position in the unused array
        # We should have an array containing all all unused elements being passed in. 
        # So for the first call we would do something like 
        # Concatenating arrays an expensive operation?

        solution = []
        selected = [False] * len(nums)

        # how do I solve this. 
        def search(curr, i):
            # print(curr, i)
            if selected[i] == True:
                # print("Exited")
                return 
            if len(curr) == len(nums):
                solution.append(curr.copy())
                return 

            if i>=0:
                selected[i] = True
            
            for idx, element in enumerate(nums):
                curr.append(element)
                search(curr, idx)
                curr.pop()
            
            selected[i] = False 
            return

        search([], -1)
        return solution