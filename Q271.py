class Solution:

    def encode(self, strs: list[str]) -> str:
        es = ""
        for word in strs:
            es += str(len(word)) + "#" + word 
            # print(es)
        return es
        
    def decode(self, s: str) -> list[str]:
        n = len(s)
        cur_str = ""
        count = 0
        prefix_found = False
        ds = []
        if s == "":
            return []
        
        for i in range(n):
            if count != 0:
                count -= 1
            elif s[i] == "#":
                count = int(cur_str)
                prefix_found = True
                cur_str = ""
            elif count == 0 and prefix_found:
                ds.append(cur_str[1:])
                cur_str = ""
                prefix_found = False
            
            cur_str += s[i]
        ds.append(cur_str[1:])
        return ds
