//64. 最小路径和
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
   public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        int** dist = new int*[m];
        for (int i = 0; i < m; i++) {
            dist[i] = new int[n];
            memset(dist[i], 0, sizeof(0) * n);
        }
        dist[0][0] = grid[0][0];
        for (int j = 1; j < n; j++) {
            dist[0][j] = grid[0][j] + dist[0][j-1];
        }
        for (int i = 1; i < m; i++) {
            int up, left;
            for (int j = 0; j < n; j++) {
                up = dist[i - 1][j];
                if (j == 0)
                    left = 0x0fffffff;
                else
                    left = dist[i][j - 1];
                int t = min(up, left) + grid[i][j];
                dist[i][j] = min(up, left) + grid[i][j];
            }
        }
        return dist[m-1][n-1];
    }
};

// int main(int argc, const char** argv) {
//     vector<vector<int>> a = {{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
//     Solution().minPathSum(a);
// }