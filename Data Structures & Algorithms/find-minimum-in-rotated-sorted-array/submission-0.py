class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        m = nums[0]
        while i < j:

            if nums[i] < nums[i+1]:
                i += 1
            
            else:
                m = min(m, nums[i + 1])
                break

            if nums[j] > nums[j - 1]:
                j -= 1
            
            else:
                m = min(m, nums[j])
                break 
        
        return m
            