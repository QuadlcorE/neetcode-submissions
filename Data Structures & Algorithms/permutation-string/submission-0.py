class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # We have to use a window with the length of s1
        # I'm assuming by permutation it must be consecutive? thus we cannot look for "abc" in "abdc"
        # so we could use a window? and sort all chars in that window? 
        # if the length of s1 is n and the length of s2 is m. 
        # m must be greater than n for this to return true
        # we would go through all chars in m up to m - n char. 
        # we would need to perform a sort m-n times.
        # so the runtime would be O((m-n)nlog(n))

        l, r = 0, len(s1)
        search_val = sorted(s1)
        
        while r <= len(s2):
            curr = sorted(s2[l:r])
            if curr == search_val: 
                return True
            l+=1
            r+=1
        
        return False
