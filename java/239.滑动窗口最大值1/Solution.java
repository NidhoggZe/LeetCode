//双向队列
import java.util.ArrayDeque;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        if (n < k)
            k = n;
        int[] res = new int[n - k + 1];
        ArrayDeque<Integer> d = new ArrayDeque<>();
        for (int i = 0; i < k; i++) {
            while (!d.isEmpty() && nums[d.getLast()] < nums[i]) 
                d.pollLast();
            d.offerLast(i);
        }
        res[0] = nums[d.getFirst()];
        for (int i = 1; i < n - k + 1; i++) {
            if (d.getFirst() < i) d.pollFirst();
            while (!d.isEmpty() && nums[d.getLast()] < nums[i + k - 1]) 
                d.pollLast();
            d.offerLast(i + k - 1);
            res[i] = nums[d.getFirst()];
        }
        return res;
    }
}