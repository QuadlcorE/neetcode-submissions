class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # We might want to use two pointers and a max value
        # for each char we check the number of changed characters we'd have if we keep changing the characters.

        chars = {}
        res = 0

        l=0

        for i in range(len(s)):
            # We need to increase the new char count after increasing the window size
            chars[s[i]] = 1 + chars.get(s[i], 0)

            # if the current window is invalid we reduce it
            # To verify if a window is valid or not we check if the dif between window length and current max(chars) is less than k
            while (i-l+1) - max(chars.values()) > k:
                # shift the left index
                chars[s[l]] -= 1
                l+=1
            
            res = max(res, i-l+1)

        return res