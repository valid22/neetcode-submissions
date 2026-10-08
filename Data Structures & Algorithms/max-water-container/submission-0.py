class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = lambda i, j: (j-i) * min(heights[i], heights[j])

        i, j = 0, len(heights) - 1

        max_w = -1

        while i < len(heights) and j > -1:
            w = water(i, j)
            if w > max_w:
                max_w = w
            
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] < heights[i]:
                j -= 1
            
            else:
                i += 1
                j -= 1
        
        return max_w
