class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, r = 0, len_min = nums.size() + 1;
        int s = 0;

        for (int i = 0; i < nums.size(); ++i) {
            s += nums[i];

            while (s >= target && l <= i) {
                len_min = min(len_min, i - l + 1);
                s -= nums[l];
                ++l;
            }
        }

        return (len_min == (nums.size() + 1)) ? 0 : len_min;
    }
};