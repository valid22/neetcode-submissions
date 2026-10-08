class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = {}

        p = {}
        for i in range(len(numbers)):
            x = numbers[i]
            r = target - x

            if r in n:
                x, r = (x, r) if x < r else (r, x)
                p[(x, r)] = p.get((x, r), 0) + 1
            
            n[x] = i
        
        return p.keys()

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        p = None
        for i, n in enumerate(nums):
            if p == n:
                continue
            
            x = self.twoSum(nums[i+1:], -n)
            
            for j in x:
                r.append([n, *j])

            p = n
        return r
            
