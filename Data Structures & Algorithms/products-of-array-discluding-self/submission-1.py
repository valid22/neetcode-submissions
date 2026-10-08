class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * len(nums)
        t = 1
        z = 0

        for i in nums:
            if i == 0:
                z += 1
                continue
            t *= i
        
        if z > 1:
            return [0] * len(nums)
        elif z == 1:
            for i in range(len(nums)):
                r[i] = t if nums[i] == 0 else 0
            
        else:
            for i in range(len(nums)):
                r[i] = t // nums[i]
        
        return r