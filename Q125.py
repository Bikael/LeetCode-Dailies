class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()
        center = len(s) // 2
        r = center
        l = center
        if len(s) % 2 == 0:
            l-=1
            
        while r < len(s) and l >= 0:
            if s[l] != s[r]:
                return False
            r+=1
            l-=1
        return True
        