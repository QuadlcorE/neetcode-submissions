class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or  
                    ord('0') <= ord(c) <= ord('9')
            )

        x = 0 
        y = len(s)-1
        while x<y:
            while not alphaNum(s[x])and x<y:
                x+=1
            while not alphaNum(s[y]) and y>x:
                y-=1
            if s[x].lower() != s[y].lower():
                return False
            x+=1
            y-=1
        
        return True