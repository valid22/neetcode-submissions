class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        c = 0
        while i <= j and -1 < i < len(nums):
            p = (j + i) // 2
            if nums[i] == target:
                return i 
            elif nums[j] == target:
                return j 
            elif nums[p] == target:
                return p
            
            if nums[p] > target:
                j = p - 1
            else:
                i = p + 1
        
        return -1