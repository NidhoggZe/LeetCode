//快速排序的patition，记得几个细节
class Solution {
    int locate(int l, int r, int[] nums) { //这里的nums[r]是参与排序的，也就是闭区间
        int curNum = nums[l];//一开始记录基准值
        while (l < r) { //虽然闭区间但是是<号，相交的位置会空出来给基准值
            while (l < r && nums[r] < curNum)
                r--;
            nums[l] = nums[r];
            while (l < r && nums[l] >= curNum)
                l++;
            nums[r] = nums[l];
        }
        nums[l] = curNum;//基准值放在最后两拨相交的位置
        return l;
    }

    public int findKthLargest(int[] nums, int k) {
        int endpos = 0, n = nums.length, l = 0, r = n-1;
        k--;
        while (true) {
            endpos = locate(l, r, nums);
            if (endpos == k)
                return nums[k];
            else if (endpos > k)
                r = endpos - 1;
            else
                l = endpos + 1;
        }
    }
}