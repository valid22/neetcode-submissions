class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bins = {i: set() for i in range(1, len(nums) + 1)}
        count = {}

        count_m = 0
        for i in nums:
            count[i] = count.get(i, 0) + 1
            count_m = max(count_m, count[i])
            if count[i] == 1:
                bins[1].add(i)
                continue
            
            bins[count[i] - 1].discard(i)
            bins[count[i]].add(i)

        top_k = []
        for i in range(count_m, 0, -1):
            if k < 1:
                break
            # bins[i] = list(bins[i])

            x = list(bins[i]) #[:k]
            top_k.extend(x)
            k -= len(x)
        
        return top_k