class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cp = prices[0];
        int max_p = 0;

        for (int i = 1; i < prices.size(); ++i) {
            max_p = max(max_p, prices[i]-cp);
            cp = min(cp, prices[i]);

            
        }

        return max_p;
    }
};
