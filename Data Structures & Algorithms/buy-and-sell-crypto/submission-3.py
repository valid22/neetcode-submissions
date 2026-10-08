class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp = sp = prices[0]

        max_profit = 0

        for p in prices[1:]:
            if p < cp:
                cp = sp = p
            elif p > sp:
                sp = p
            
            max_profit = max(max_profit, sp-cp)
        
        return max_profit

        