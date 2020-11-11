class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) return 0;
        int maxlastlast = 0, maxlast = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int maxcur = Math.max(maxlastlast + nums[i], maxlast);
            maxlastlast = maxlast;
            maxlast = maxcur;
        }
        return maxlast;
    }
}