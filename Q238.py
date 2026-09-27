class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        occur = {}
        product = 1
        prod_list = []

        for i in range(n):
            if nums[i] != 0:
                product *= nums[i]
            if nums[i] not in occur:
                occur[nums[i]] = 0
            occur[nums[i]] += 1
        
        if 0 in occur:
            if occur[0] > 1:
                return [0] * n
            else:
                for i in range(n):
                    if nums[i] == 0:
                        prod_list.append(product)
                    else:
                        prod_list.append(0)
        else:
            for i in range(n):
                prod_list.append(int(product/nums[i]))
        
        return prod_list
            