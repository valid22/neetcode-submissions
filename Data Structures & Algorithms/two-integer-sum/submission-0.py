class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ni = {}
        for i, n in enumerate(nums):
            r = target - n
            if r in ni:
                return [ni[r], i]
            ni[n] = i