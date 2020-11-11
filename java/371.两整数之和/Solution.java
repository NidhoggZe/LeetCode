class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int tempa = a ^ b;
            int tempb = (a & b) << 1;
            a = tempa;
            b = tempb;
        }
        return a;
    }
}