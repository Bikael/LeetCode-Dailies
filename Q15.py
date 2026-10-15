
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s_nums = sorted(nums)
        ret_list = []

        for i in range(n - 2):

            if i > 0 and s_nums[i] == s_nums[i - 1]:
                continue

            l = i + 1
            r = n - 1

            while l < r:
                total = s_nums[i] + s_nums[l] + s_nums[r]

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ret_list.append([s_nums[i], s_nums[l], s_nums[r]])
                    l += 1
                    r -= 1

                    while l < r and s_nums[l] == s_nums[l - 1]:
                        l += 1

                    while l < r and s_nums[r] == s_nums[r + 1]:
                        r -= 1

        return ret_list
