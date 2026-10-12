class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {0: 1} # prefix_sum -> count

        count = 0
        s = 0
        
        for i in range(len(nums)):
            s += nums[i]

            if (s - k) in prefix_map:
                count += prefix_map[s - k]

            prefix_map[s] = prefix_map.get(s, 0) + 1

        return count