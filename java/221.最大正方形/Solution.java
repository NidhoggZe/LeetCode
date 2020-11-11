class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix.length == 0) return 0;
        int row = matrix.length, col = matrix[0].length, max = 0;
        int[][] res = new int[row][col];
        for (int i = 0; i < row; i++) {
            int cur = matrix[i][0] - '0';
            max += cur;
            res[i][0] = cur;
        }
        for (int i = 0; i < col; i++) {
            int cur = matrix[0][i] - '0';
            max += cur;
            res[0][i] = cur;
        }
        if (max > 0) max = 1;
        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                if (matrix[i][j] == '1')
                    res[i][j] = Math.min(Math.min(res[i][j-1], res[i-1][j]), res[i-1][j-1]) + 1;
                else
                    res[i][j] = 0;
                max = Math.max(max, res[i][j]);
            }
        }
        return max*max;
    }
}