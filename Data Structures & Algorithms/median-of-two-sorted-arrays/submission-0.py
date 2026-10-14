class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        i = j = 0
        prev = curr = 0

        for _ in range((m + n) // 2 + 1):
            prev = curr

            if j >= n or (i < m and nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if (m + n) % 2:
            return curr

        return (prev + curr) / 2