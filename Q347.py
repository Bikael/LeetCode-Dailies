class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        occur = {}
        k_list = []

        buckets = [[] for _ in range(n)]

        for i in range(n):
            if nums[i] not in occur:
                occur[nums[i]] = 0
            occur[nums[i]] += 1

        # print(occur)
        for key in occur:
            # print(f"key: {key}")
            buckets[occur[key] -1].append(key)


        # print(buckets)
        for i in range(n-1,-1,-1):
            for j in range(len(buckets[i-1])):
                k_list.append(buckets[i-1][j])
            if len(k_list) == k:
                break
        # print(k_list)
        
        return k_list
