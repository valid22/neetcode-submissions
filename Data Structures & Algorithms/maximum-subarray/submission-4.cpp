class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur_sum = -10001, max_sum = -10001;

        for (int &i: nums) {
            cur_sum += i;
            
            if (cur_sum < i) {
                cur_sum = i;
            }

            if (cur_sum > max_sum) {
                max_sum = cur_sum;
            }
        }

        return max_sum;
    }
};
