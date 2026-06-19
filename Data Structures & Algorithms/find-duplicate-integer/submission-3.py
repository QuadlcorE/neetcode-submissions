class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # So considering I have duplicates 
        # I cannot use a hash set 
        # I cannot also modify the values 
        # We utilize the fast and slow pointers to identify the start of a loop 
        # We treat each entry in the array as a node that points to another node. 
        # So for the fast and slow pointer we do two sets 
        # first the fast & slow and then the slow & slow pointer. 
        fast, slow = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        # Then we start a new slow pointer which will meet our intersection at the start of the loop 
        # We do the if check only after the first change because we know the first node can not be start of the loop. 
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow