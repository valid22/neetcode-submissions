class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1

        while i < j:
            mid = (i + j) // 2

            if nums[mid] > nums[j]:
                # Minimum must be to the right of mid
                i = mid + 1
            else:
                # mid could itself be the minimum
                j = mid

        return nums[i]