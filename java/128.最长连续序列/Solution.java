import java.util.HashSet;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0)
            return 0;
        HashSet<Integer> s = new HashSet<Integer>();
        for (int i : nums) {
            s.add(i);
        }
        int maxlength = 1;
        int curlength = 1;
        for (int i : s) {
            curlength = 1;
            if (!s.contains(i - 1)) {
                int j = i + 1;
                while (s.contains(j++)) {
                    curlength++;
                }
                maxlength = Math.max(maxlength, curlength);
            }
        }
        return maxlength;
    }
}