class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = [1]
        x = nums[0]
        for i in nums[1:]:
            p.append(p[-1] * x)
            x = i
        
        s = [1]
        x = nums[-1]
        for i in nums[-2::-1]:
            s.append(s[-1] * x)
            x = i

        s = s[::-1]
        return [p[i] * s[i] for i in range(len(nums))]