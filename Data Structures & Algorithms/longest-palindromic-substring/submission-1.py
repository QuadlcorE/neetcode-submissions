class Solution:
    def longestPalindrome(self, s: str) -> str:
        # We need to cycle through and check each letter as the possible center of a palindrome
        startIndex = 0
        LongestLength = 0

        for index in range(len(s)):
            # Odd index
            width = 0
            while ( index-width >= 0 and index+width < len(s) and s[index-width] == s[index+width]):
                # Update the longest length
                curr_length = width + width + 1
                if ( curr_length > LongestLength):
                    startIndex = index-width
                    LongestLength = curr_length
                width +=1
            
            #Even index
            l, r = index, index+1
            width = 0
            while (l-width >= 0 and r+width < len(s) and s[l-width] == s[r+width]):
                # Update the longest length 
                curr_length = width + width + 2
                if ( curr_length > LongestLength ):
                    startIndex = l-width
                    LongestLength = curr_length
                width += 1
        
        return s[startIndex:startIndex+LongestLength]