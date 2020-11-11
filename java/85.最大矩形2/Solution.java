import java.util.Arrays;

class Solution {

    public int maximalRectangle(char[][] matrix) {
        int m = matrix.length;
        if (m == 0)
            return 0;
        int n = matrix[0].length;

        int[] left = new int[n], right = new int[n], height = new int[n];
        Arrays.fill(right, n);

        int maxarea = 0;
        for (int i = 0; i < m; i++) {
            int curLeft = 0, curRight = n;

            for (int j = n - 1; j >= 0; j--) {
                if (matrix[i][j] == '1')
                    right[j] = Math.min(right[j], curRight);
                else {
                    right[j] = n;
                    curRight = j;
                }
            }

            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1')
                    height[j]++;
                else
                    height[j] = 0;

                if (matrix[i][j] == '1')
                    left[j] = Math.max(left[j], curLeft);
                else {
                    left[j] = 0;
                    curLeft = j + 1;
                }

                maxarea = Math.max(maxarea, (right[j] - left[j]) * height[j]);
            }
        }
        return maxarea;
    }
}