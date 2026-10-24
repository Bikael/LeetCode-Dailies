class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        print(nums)
        while l <= r:
            mid = (r+l) // 2
            # print(f"l: {l}")
            # print(f"r: {r}")
            # print(f"mid: {mid}")
            if nums[mid] == target:
                # print(f"mid is equal to r")
                return mid
            
            if nums[mid] > nums[r]:
                # print(f"mid is bigger than r")
                if target > nums[mid] or target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # print(f"mid is smaller than r")
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

