import java.util.ArrayList;

class Solution {

    void searchAdd(ArrayList<Integer> arr, int num) {
        int l = 0, r = arr.size(), mid = (l + r) / 2;
        while (l < r) {
            if (arr.get(mid) == num)
                return;
            else if (arr.get(mid) < num)
                l = mid + 1;
            else
                r = mid;
            mid = (l + r) / 2;
        }
        arr.set(mid, num);
        return;
    }

    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0)
            return 0;
        int maxl = 1;
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(nums[0]);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > arr.get(arr.size() - 1)) {
                arr.add(nums[i]);
                maxl++;
            } else
                searchAdd(arr, nums[i]);
        }

        return maxl;
    }
}
