class Solution {
    public int minDistance(String word1, String word2) {
        int l1 = word1.length();
        int l2 = word2.length();
        int[][] d = new int[l1 + 1][l2 + 1];
        for (int i = 0; i < l1 + 1; i++) {
            d[i][0] = i;
        }
        for (int i = 0; i < l2 + 1; i++) {
            d[0][i] = i;
        }
        for (int i = 1; i < l1 + 1; i++) {
            for (int j = 1; j < l2 + 1; j++) {
                int up = d[i - 1][j] + 1;
                int left = d[i][j - 1] + 1;
                int upleft = d[i - 1][j - 1] + 1;
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    upleft--;
                }
                d[i][j] = Math.min(upleft, Math.min(up, left));
            }
        }
        return d[l1][l2];
    }
}