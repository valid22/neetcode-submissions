class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = [-1] * 2001

        for i in range(len(numbers)):
            x = numbers[i]
            r = target - x

            if n[r] != -1:
                return [min(i, n[r]) + 1, max(i, n[r]) + 1]
            
            n[x] = i
        
        