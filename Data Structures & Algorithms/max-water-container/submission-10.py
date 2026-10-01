class Solution:
    def maxArea(self, heights: List[int]) -> int:
        c1 = 0
        c2 = len(heights) - 1 

        max = 0

        while (c2 > c1):
            volume = ((c2 - c1) * min(heights[c1], heights[c2]))
            if max < volume:
                max = volume
            
            if heights[c1] < heights[c2]:
                c1 += 1
            else:
                c2 -=1
            
        return max