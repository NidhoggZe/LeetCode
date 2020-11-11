//62. 不同路径
/*排列组合知识：n个小球放入m个盒子
1.球同，盒不同，不能空，等价于一共有n-1个空隙
，要插m-1个板C(m-1,n-1)（本题是把插板变为小球套公式）
2.球同，盒不同，能空。如果给每个盒子一个球，就可以把问题转化为不能空的情况了,就相当于n+m个小球放入m个盒子且不能空，C(m-1,n+m-1)
*/

using namespace std;

class Solution {
   public:
    int uniquePaths(int m, int n) {
        if (n < m) {
            int t = n;
            n = m;
            m = t;
        }
        n = m + n - 2;
        m = m - 1;
        long long k = 1, l = 1;
        for (int i = 0; i < m; i++) {
            k *= (n - i);
            l *= (1 + i);
        }
        return k / l;
    }
};
