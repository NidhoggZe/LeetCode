class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0) return false;
        int row = matrix.length,  col = matrix[0].length, m = row - 1, n = 0;
        while (m >= 0 && n < col) {
            int curNum = matrix[m][n];
            if (curNum == target) return true;
            else if (curNum < target) n++;
            else m--;
        }
        return false;
    }
}