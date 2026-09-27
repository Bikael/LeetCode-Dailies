class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur_s = {}
        occur_t = {}

        for char in t:
            if char not in occur_t:
                occur_t[char] = 1
            else:
                occur_t[char] += 1
        
        for char in s:
            if char not in occur_s:
                occur_s[char] = 1
            else:
                occur_s[char] += 1

        if occur_t == occur_s:
            return True
        return False