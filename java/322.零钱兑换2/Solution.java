import java.util.Arrays;

//自底向上
class Solution {

    public int coinChange(int[] coins, int amount) {
        if (amount == 0)
            return 0;
        int[] count = new int[amount + 1];
        Arrays.fill(count, amount + 1);
        count[0] = 0;
        for (int i = 1; i < count.length; i++) {
            for (int j = 0; j < coins.length; j++) {
                if (i >= coins[j])
                    count[i] = Math.min(count[i], count[i - coins[j]] + 1);
            }
        }
        return count[amount] == amount + 1 ? -1 : count[amount];
    }
}