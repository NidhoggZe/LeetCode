class Solution {
    public int divide(int dividend, int divisor) {
        boolean ispos = true;
        if ((dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0))
            ispos = false;
        if (dividend > 0)
            dividend = -dividend;
        if (divisor > 0)
            divisor = -divisor;
        int res = 0;
        while (dividend <= divisor) {
            int curdiv = divisor;
            int count = -1;
            while (curdiv > (dividend >> 1)) {
                curdiv <<= 1;
                count <<= 1;
            }
            res += count;
            dividend -= curdiv;
        }

        if (ispos)
            res = res <= Integer.MIN_VALUE ? Integer.MAX_VALUE : -res;

        return res;
    }
}