class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cp = prices[0];
        int sp = prices[0];

        int max_p = 0;

        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] < cp) {
                cp = sp = prices[i];
            } else if (prices[i] > sp) {
                sp = prices[i];
            }

            max_p = max(max_p, sp-cp);
        }

        return max_p;
    }
};
