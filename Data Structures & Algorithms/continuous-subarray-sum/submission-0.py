class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        r = {0: -1}
        t = 0

        for i, n in enumerate(nums):
            t += n
            ri = t % k 
            if ri not in r:
                r[ri] = i
            elif i - r[ri] > 1:
                return True
            
        
        return False