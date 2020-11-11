import java.util.HashMap;
import java.util.Map;

class Solution {
    int partition(int[][] nums, int l, int r) {
        int base = nums[l][1];
        int[] cache = nums[l];
        while (l < r) {
            while (l < r && nums[r][1] < base) r--;
            nums[l] = nums[r];
            while (l < r && nums[l][1] >= base) l++;
            nums[r] = nums[l];
        }
        nums[l] = cache;
        return l;
    }

    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        int[][] count = new int[map.size()][2];
        int i = 0;
        for (Map.Entry<Integer, Integer> en : map.entrySet()) {
            count[i] = new int[]{en.getKey(), en.getValue()};
            i++;
        }
        int target = k, ret = 0, l = 0, r = count.length - 1;
        while (ret + 1 != target) {
            ret = partition(count, l, r);
            if (ret + 1 > k) 
                r = ret - 1;
            else l = ret + 1;
        }
        int[] res = new int[k];
        for (int j = 0; j < k; j++) {
            res[j] = count[j][0];
        }
        return res;
    }
}