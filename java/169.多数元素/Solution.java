class Solution {
    public int majorityElement(int[] nums) {
        int curnum = 0;
        int count = 0;
        for (int i : nums) {
            if (count == 0) curnum = i;
            if (i == curnum) count++;
            else count--;
        }
        return curnum;
    }
}