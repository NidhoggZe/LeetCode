//自顶向下
class Solution {
    int[] count;

    int dfs(int[] coins, int rest) {
        if (rest < 0)
            return -1;
        if (rest == 0)
            return 0;
        if (count[rest] != 0)
            return count[rest];
        int min = rest + 1;
        for (int i = coins.length - 1; i >= 0; i--) {
            int cur = dfs(coins, rest - coins[i]) + 1;
            if (cur > 0)
                min = Math.min(min, cur);
        }
        if (min == rest + 1) {
            count[rest] = -1;
            return -1;
        } else {
            count[rest] = min;
            return min;
        }
    }

    public int coinChange(int[] coins, int amount) {
        if (amount == 0)
            return 0;
        count = new int[amount + 1];
        // count[0] = 0;
        dfs(coins, amount);
        return count[amount];
    }
}