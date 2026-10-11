class Solution {
public:

    void islandsAndTreasure(vector<vector<int>>& grid) {

        const int INF = 2147483647,
            WATER = -1,
            CHEST = 0;
        
        const int m = grid.size(), n = grid[0].size();
        const std::vector<std::tuple<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        std::queue<std::tuple<int, int>> qu;

        auto is_valid = [INF, m, n, &grid](int i, int j) {
            return -1 < i && i < m && -1 < j && j < n && (grid[i][j] == INF);
        };

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == CHEST) {
                    qu.push({i, j});
                }
            }
        }

        int z = 0;
        while (!qu.empty()) {
            auto cell = qu.front();
            qu.pop();
            ++z;
            int p = std::get<0>(cell), q = std::get<1>(cell);

            for (auto &d:dir) {
                int x = p + std::get<0>(d), y = q + std::get<1>(d);
                if (is_valid(x, y)) {
                    grid[x][y] = grid[p][q] + 1;
                    qu.push({x, y});
                }
            }

            // if (z == 50) break;
        }

    }
};
