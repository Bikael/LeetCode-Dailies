def lengthOfLongestSubstring( s: str) -> int:
    index = 0
    dupe_map = {}
    longest_sub_array = 0

    while index < len(s):
        if s[index] not in dupe_map:
            dupe_map[s[index]] = index
        else:  
            index = dupe_map[s[index]]
            dupe_map = {}
            dupe_map[s[index]] = index + 1
            
        if len(dupe_map) > longest_sub_array:
            longest_sub_array = len(dupe_map)

        index += 1

        
            
            
lengthOfLongestSubstring("1R1T7")