def lengthOfLongestSubstring( s: str) -> int:
    longest_sub_array = 0
    dupe_map = {}
    start = 0
    end = 0

    while end < len(s):

        if s[end] not in dupe_map:
            dupe_map[s[end]] = end
        else:
            start = max(start, dupe_map[s[end]] + 1)
            dupe_map[s[end]] = end
            
        end += 1

        if longest_sub_array < end - start:
            longest_sub_array = end - start

    print(longest_sub_array)
    return longest_sub_array

lengthOfLongestSubstring("eea")