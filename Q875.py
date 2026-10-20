class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        mid = 0
        while l<=r:      
            mid = (l+r) // 2
            total_time = 0
            for pile in piles:
                total_time += math.ceil(pile/mid)
            if total_time <= h:
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid+1
        return res
