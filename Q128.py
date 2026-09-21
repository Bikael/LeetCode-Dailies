def longestConsecutive(nums: list[int]) -> int:
        num_set = set(nums)
        cur_seq = 1
        lcs = 1

        if nums == []:
            return 0 
        for num in nums:
            while num + 1 in num_set:
                cur_seq += 1
                num += 1

            if cur_seq >= lcs:
                lcs = cur_seq
            cur_seq = 1    

            while num - 1 in num_set:
                cur_seq += 1
                num -= 1

            if cur_seq >= lcs:
                lcs = cur_seq
            cur_seq = 1  
            

            
        return lcs

print(longestConsecutive([100,4,200,1,3,2]))