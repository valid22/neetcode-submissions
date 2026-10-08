class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int cp = prices[0];
        int max_p = 0;

        for (int &i: prices) {
            max_p = max(max_p, i-cp);
            cp = min(cp, i);

            
        }

        return max_p;
    }
};
