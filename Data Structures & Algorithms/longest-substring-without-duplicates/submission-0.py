class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        mem = set()
        maxc = 0
        for r, char in enumerate(s):
            if char not in mem:
                mem.add(char)
            else:
                while (char in mem):
                    mem.remove(s[l])
                    l+=1
                mem.add(char)
            maxc = max(r-l+1, maxc)
        return maxc