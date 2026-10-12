class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end());
        vector<vector<int>> sorted{intervals[0]};

        const int n = intervals.size();
        for (int i = 1; i < n; ++i) {
            if (intervals[i][0] <= sorted[sorted.size() - 1][1]) {
                sorted[sorted.size() - 1][1] = std::max(sorted[sorted.size() - 1][1], intervals[i][1]);
            } else {
                sorted.push_back(intervals[i]);
            }
        }

        return sorted;
    }
};
