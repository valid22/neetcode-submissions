class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = i = 0
        len_min = float('inf')
        
        s = 0

        while i < len(nums):
            s += nums[i]

            while s >= target:
                len_min = min(len_min, i - l+1)
                s -= nums[l]
                l += 1

                
            i += 1
        
        return 0 if len_min == float('inf') else len_min