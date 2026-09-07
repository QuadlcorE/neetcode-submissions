class Solution:
    def countSubstrings(self, s: str) -> int:
        # We have to go through all substrings so it's worth it to consider that
        # For every single palindrome we find we have to increment the count. 

        palindromicCount = 0

        for i in range(len(s)):
            # odd count
            l, r = i, i
            while l>=0 and r< len(s) and s[l] == s[r]:
                palindromicCount += 1
                l -=1 
                r +=1
            
            # even count
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                palindromicCount += 1
                l -= 1
                r += 1
        
        return palindromicCount