# had to watch youtube video on how to do this sets are op

def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    lcs = 1
    cur_seq = 1

    if nums == []:
        return 0
    
    for num in num_set:
        if num + 1 in num_set and num - 1 not in num_set:
            while num + 1 in num_set:
                cur_seq += 1
                num += 1

            if cur_seq >= lcs:
                lcs = cur_seq
            cur_seq = 1
    return lcs

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))