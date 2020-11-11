class Solution {
    public int myAtoi(String s) {
        int res = 0;
        boolean isneg = false;
        char[] ss = s.strip().toCharArray();
        if (ss.length == 0)
            return 0;
        int i = 0;
        if (ss[0] == '-') {
            isneg = true;
            i++;
        }
        else if (ss[0] == '+')
            i++;
        else if (!Character.isDigit(ss[0]))
            return 0;
        
        for (; i < ss.length && Character.isDigit(ss[i]); i++) {
            int curnum = ss[i]-'0';
            if (res < Integer.MIN_VALUE/10 || (res == Integer.MIN_VALUE/10 && curnum > 8)) {
                res = Integer.MIN_VALUE;
                break;
            }
            res = res * 10 - curnum;
        }

        if (!isneg) {
            if (res == Integer.MIN_VALUE)
                return Integer.MAX_VALUE;
            else
                return -res;
        }

        return res;


    }
}