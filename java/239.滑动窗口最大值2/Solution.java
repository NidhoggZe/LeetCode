class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        if (n < k) k = n;
        int[] left = new int[n], right = new int[n];
        int max = 0;
        for (int i = 0; i < n; i++) {
            if (i % k == 0)
                max = nums[i];
            else
                max = Math.max(nums[i], max);
            left[i] = max;
        }
        max = nums[n-1];
        for (int i = n-1; i >= 0; i--){
            if (i % k == k-1)
                max = nums[i];
            else
                max = Math.max(nums[i], max);
            right[i] = max; 
        }
        int[] res = new int[n - k + 1];
        for (int i = 0; i < res.length; i++) {
            res[i] = Math.max(right[i], left[i + k - 1]);
        }

        return res;
    }
}