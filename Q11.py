class Solution:
    def maxArea(self, height: list[int]) -> int:
        mv = 0
        n = len(height)
        r = n-1
        l = 0

        while l != r:
            h = min(height[l], height[r])
            if  h * (r-l) > mv:
                mv = h * (r-l)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return mv