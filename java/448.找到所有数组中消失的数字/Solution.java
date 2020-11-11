import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        for (int i = 1; i <= nums.length; i++) {
            int cur = nums[i - 1];
            while (cur > 0) {
                int next = nums[cur - 1];
                nums[cur - 1] = -1;
                cur = next;
            }
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0)
                res.add(i + 1);
        }
        return res;
    }
}

