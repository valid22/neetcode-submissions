class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int r = 0, m = matrix.size(), n = matrix[0].size();
        while (r < m) {
            std::cout << "r = " << r << " | " << m << "\n";
            if (matrix[r][0] > target) break;
            ++r;
        }
        if (r == 0) return false;
        
        --r;
        for (int c = 0; c < n; ++c) {
            if (matrix[r][c] == target) {
                return true;
            }
        }

        return false;
    }
};
