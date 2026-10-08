class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bins = {i: [] for i in range(1, len(nums) + 1)}
        count = {}

        count_m = 0
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for i, x in count.items():
            bins[x].append(i)

        top_k = []
        for i in range(len(nums), 0, -1):
            if k < 1:
                break
            # bins[i] = list(bins[i])

            x = bins[i] #[:k]
            top_k.extend(x)
            k -= len(x)
        
        return top_k