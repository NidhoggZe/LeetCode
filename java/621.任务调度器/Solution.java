import java.util.Arrays;

class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] map = new int[26];
        for (int i = 0; i < tasks.length; i++) {
            map[tasks[i] - 'A']++;
        }
        Arrays.sort(map);
        int max = map[25], time = (max - 1) * n + 1, cap = (max - 1) * (n - 1);
        for (int i = 24; i >= 0 && map[i] > 0; i--) {
            if (map[i] == max) {
                time++;
                map[i]--;
            }
            cap -= map[i];
        }
        return cap >= 0 ? time : tasks.length;
    }
}