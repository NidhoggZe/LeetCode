
//48. 旋转图像
using namespace std;
#include <vector>

class Solution {
   public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int i = 0; i < n/2; i++) {
            for (int j = i; j < n - 1 - i; j++) {
                int t1 = matrix[i][j], t2 = matrix[j][n-1-i], t3 = matrix[n-1-i][n-1-j], t4 = matrix[n-1-j][i];
                matrix[i][j] = t4;
                matrix[j][n-1-i] = t1;
                matrix[n-1-i][n-1-j] = t2;
                matrix[n-1-j][i] = t3;
            }            
        }
        return;
    }
};