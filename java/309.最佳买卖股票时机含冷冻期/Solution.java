class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if (n == 0) return 0;
        int[] profit = {-prices[0], 0, 0};
        int maxprofit = 0;
        for (int i = 0; i < n; i++) {
            int profit0 = Math.max(profit[0], profit[2] - prices[i]);
            int profit1 = profit[0] + prices[i];
            int profit2 = Math.max(profit[1], profit[2]);

            profit[0] = profit0;
            profit[1] = profit1;
            profit[2] = profit2;
            maxprofit = Math.max(maxprofit, profit[1]);
        }
        return maxprofit;
    }
}