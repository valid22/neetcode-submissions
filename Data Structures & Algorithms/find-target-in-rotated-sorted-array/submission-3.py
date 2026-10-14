class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[i] <= nums[mid]:

                # Target is inside the sorted left half
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1

            # Right half is sorted
            else:

                # Target is inside the sorted right half
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        return -1