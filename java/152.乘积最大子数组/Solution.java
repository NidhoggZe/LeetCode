class Solution {
    public int maxProduct(int[] nums) {
        int maxpos = nums[0];
        int maxneg = nums[0];
        int max = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            int temppos = Math.max(num, Math.max(num*maxpos, num*maxneg));
            int tempneg = Math.min(num, Math.min(num*maxpos, num*maxneg));
            maxpos = temppos;
            maxneg = tempneg;
            max = Math.max(max, maxpos);
        }
        return max;
    }
}