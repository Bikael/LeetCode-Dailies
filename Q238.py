class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        l_prod = []
        r_prod = []
        ret_list = []

        for i in range(n):
            if i == 0:
                l_prod.append(prod)
            else:
                prod *= nums[i-1]
                l_prod.append(prod)

            
        # print(l_prod)

        prod = 1

        for i in range(n-1,-1,-1):
            if i == n-1:
                r_prod.append(prod)
            else:
                prod *= nums[i+1]
                r_prod.append(prod)

        # print(r_prod)

        for i in range(n):
            ret_list.append(l_prod[i] * r_prod[n-i-1])

        return ret_list