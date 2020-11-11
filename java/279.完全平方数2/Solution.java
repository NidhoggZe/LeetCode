import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int numSquares(int n) {
        int sqr = (int) Math.sqrt(n);
        int[] sqr2 = new int[sqr];
        for (int i = 0; i < sqr; i++) {
            sqr2[i] = (i + 1) * (i + 1);
        }
        int step = 0;
        Queue<Integer> curTurn = new LinkedList<>();
        curTurn.offer(n);
        while (true) {
            step++;
            if (!curTurn.isEmpty()) {
                int m = curTurn.size();
                for (int j = 0; j < m; j++) {
                    int curN = curTurn.poll();
                    for (int i = sqr - 1; i >= 0; i--) {
                        int t = curN - sqr2[i];
                        if (t == 0)
                            return step;
                        else if (t < 0)
                            continue;
                        else
                            curTurn.offer(t);
                    }
                }
            } else
                break;
        }
        return n;
    }
}