class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dupes = set()
        for num in nums:
            if num in dupes:
                return True
            else:
                dupes.add(num)
        return False