class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = float('-inf')
        max_sum = float('-inf')
        for i in nums:
            curSum = max(i, curSum + i)
        
            if curSum > max_sum:
                max_sum = curSum

        return int(max_sum)