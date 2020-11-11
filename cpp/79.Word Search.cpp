//79. 单词搜索
//二维平面上通过连续的字母格子找单词是否存在，由于要回溯只能dfs
#include <vector>
#include <string>
using namespace std;

class Solution {
    bool endflag = false;
    string word;
    vector<vector<char>> board;
    int row, col;

   public:
    void dfs(int n, int posi, int posj, vector<vector<bool>>& ex) {
        if (endflag) return;

        if (n == word.length()) {
            endflag = true;
            return;
        }

        if (posi < 0 || posi >= row || posj < 0 || posj >= col ||
            word[n] != board[posi][posj] || ex[posi][posj])
            return;

        ex[posi][posj] = true;
        dfs(n + 1, posi + 1, posj, ex);
        dfs(n + 1, posi - 1, posj, ex);
        dfs(n + 1, posi, posj + 1, ex);
        dfs(n + 1, posi, posj - 1, ex);
        ex[posi][posj] = false;
        return;
    }

    bool exist(vector<vector<char>>& board, string word) {
        row = board.size();
        col = board[0].size();
        this->word = word;
        this->board = board;

        vector<vector<bool>> ex(row, vector<bool>(col, false));

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == word[0]) {
                    dfs(0, i, j, ex);
                    if (endflag) return true;
                }
            }
        }
        return false;
    }
};