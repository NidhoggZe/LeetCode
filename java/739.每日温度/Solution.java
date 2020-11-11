import java.util.Stack;

class Solution {
    public int[] dailyTemperatures(int[] T) {
        int[] res = new int[T.length];
        Stack<Integer> s = new Stack<>();
        for (int i = 0; i < res.length; i++) {
            while (!s.empty() && T[s.peek()] < T[i])
                res[s.peek()] = i - s.pop();
            s.push(i);
        }
        return res;
    }
}
