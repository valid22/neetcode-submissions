class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int N = matrix.size();

        for (int l = 0; l < N/2; ++l) {
            for (int i = 0; i < (N - 1 - 2 * l); ++i) {
                int j = i + l;
                
                swap(matrix[l][j], matrix[N - 1 - j][l]);
                swap(matrix[N - 1 - j][l], matrix[N - 1 - l][N - 1 - j]);
                swap(matrix[N - 1 - l][N - 1 - j], matrix[j][N - 1 - l]);
                // swap(matrix[i][N - (l + 1)]);
            }
        }
    }
};
