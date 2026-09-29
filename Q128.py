class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        lc = 1
        count = 1

        if not nums:
            return 0

        for num in nums:
            if num + 1 in nums and num - 1 not in nums:
                while num + 1 in nums:
                    count += 1
                    num += 1
            if count > lc:
                lc = count
            count = 1

        return lc

        