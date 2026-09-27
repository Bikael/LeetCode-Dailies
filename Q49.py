class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anas = []
        added = False
        def isAnagram(s1,s2):
            occur_s1={}
            occur_s2={}

            for c in s1:
                if c not in occur_s1:
                    occur_s1[c] = 1
                else:
                    occur_s1[c] +=1

            for c in s2:
                if c not in occur_s2:
                    occur_s2[c] = 1
                else:
                    occur_s2[c] +=1
            if occur_s1 == occur_s2:
                return True
            return False

        for word in strs:
            # print(f"word: {word}")
            if not anas:
                # print(f"word added: {word}")
                anas.append([word])
            else:
                for group in anas:
                    # print(f"group: {group}")
                    if isAnagram(group[0],word):
                        group.append(word)
                        # print(f"word added: {word}")
                        added = True
                        break
                if not added:
                    anas.append([word])
                added = False
                # print(f"anas: {anas}")
        return anas
            