class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anas = {}
        anas_list = []
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anas:
                anas[key] = [word]
            else:
                anas[key].append(word)
        for key in anas:
            anas_list.append(anas[key])
        return anas_list