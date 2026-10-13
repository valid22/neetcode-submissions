class Solution:
    def trap(self, height: List[int]) -> int:
        waters = 0

        left_height = [height[0]]
        for i in height[1:]:
            left_height.append(max(left_height[-1], i))
        
        right_height = [height[-1]]
        for i in height[-2::-1]:
            right_height.append(max(right_height[-1], i))
        
        right_height = right_height[::-1]

        for i in range(len(height)):
            waters += max(0, min(left_height[i], right_height[i]) - height[i])
        

        return waters