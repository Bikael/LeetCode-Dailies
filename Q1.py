def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            # print(f"printing nums[i]: {nums[i]}")
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                # print(f"printing nums[j]: {nums[j]}")
        