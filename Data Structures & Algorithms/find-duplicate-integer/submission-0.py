class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = [0] * len(nums)
        for i in nums:
            a[i] += 1
            if a[i] > 1:
                return i 
        
        return -1