class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length, muti = 1;
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = muti;
            muti *= nums[i];
        }
        muti = 1;
        for (int i = n - 1; i >= 0; i--) {
            res[i] *= muti;
            muti *= nums[i];
        }
        return res;
    }
}