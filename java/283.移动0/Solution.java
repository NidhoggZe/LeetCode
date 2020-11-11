class Solution {
    public void moveZeroes(int[] nums) {
        int j = 0;
        while (j < nums.length && nums[j] != 0) j++;
        if (j == nums.length) return;
        int i = j + 1;
        while (i < nums.length) {
            if (nums[i] == 0) i++;
            else{
                nums[j] = nums[i];
                nums[i] = 0;
                i++;
                while (j < nums.length && nums[j] != 0) j++;
                i = Math.max(i, j);
            }
        }
        return;
    }
}