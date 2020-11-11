import java.util.List;
import java.util.ArrayList;

// 将剪枝发挥到极致的一道题
// 1.对错误的左括号右括号进行了计数，不到0没必要算是否valid
// 2.为避免对同一位反复删减，对某位决定删/不删后，后续dfs从下一位开始。
// 3.精髓1,提前计算出左右括号各有多少个需要删减的，当减的超过这个数目时必然不合题意
// 用isDelete进行记录，避免进行字符串操作，也保证能随时查询当前字符串那些位被删减了
// 4.精髓2，一连串的同种括号只删第一个，避免对同一种字符串反复判断valid并dfs。
class Solution {

    List<String> res = new ArrayList<>();

    boolean isValid(char[] str, boolean[] isDelete) {
        int count = 0;
        for (int i = 0; i < str.length; i++) {
            if (isDelete[i]) {
                continue;
            }
            if (str[i] == '(') {
                count++;
            } else if (str[i] == ')') {
                count--;
            }
            if (count < 0) {
                return false;
            }
        }
        return count == 0;
    }

    void backtrace(char[] str, int curr, int l, int r, boolean[] isDelete) {
        if (l == 0 && r == 0) {
            if (isValid(str, isDelete)) {
                StringBuilder newstr = new StringBuilder();
                for (int i = 0; i < str.length; i++) {
                    if (!isDelete[i])
                        newstr.append(str[i]);
                }
                res.add(newstr.toString());
            }
        }
        if (r > 0) {//精髓1，删的多了就不删了
            for (int i = curr; i <= str.length - l - r; i++) {
                if (str[i] == ')') {
                    if (i > curr && str[i] == str[i - 1] && isDelete[i - 1] == false) {  
                        //精髓2，一连串的同种括号只删第一个，避免对同一种字符串反复判断valid并dfs（注意理解这个false）
                        continue;
                    }
                    isDelete[i] = true;
                    backtrace(str, i + 1, l, r - 1, isDelete);
                    isDelete[i] = false;
                }
            }
        } else if (l > 0) {
            for (int i = curr; i <= str.length - l; i++) {
                if (str[i] == '(') {
                    if (i > curr && str[i] == str[i - 1] && isDelete[i - 1] == false) {
                        continue;
                    }
                    isDelete[i] = true;
                    backtrace(str, i + 1, l - 1, r, isDelete);
                    isDelete[i] = false;
                }
            }
        }
    }

    public List<String> removeInvalidParentheses(String s) {
        char[] str = s.toCharArray();
        int l = 0, r = 0;
        for (char c : str) {
            if (c == '(') {
                l++;
            } else if (c == ')') {
                if (l > 0) {
                    l--;
                } else {
                    r++;
                }
            }
        }
        boolean[] isDelete = new boolean[str.length];
        backtrace(str, 0, l, r, isDelete);
        return res;
    }
}

//BFS，自带最短长度剪枝，但是因为new太多还是慢很多，而且队列占用内存比DFS大很多
// class Solution {
//     boolean isValid(boolean[] stat, char[] s) {
//         int count = 0;
//         for (int i = 0; i < s.length; i++) {
//             if (stat[i] == true)
//                 continue;
//             if (s[i] == '(')
//                 count++;
//             else if (s[i] == ')')
//                 count--;
//             if (count < 0)
//                 return false;
//         }
//         return count == 0;
//     }

//     public List<String> removeInvalidParentheses(String str) {
//         List<String> res = new ArrayList<>();

//         char[] s = str.toCharArray();

//         int l = 0, r = 0;
//         for (int i = 0; i < s.length; i++) {
//             if (s[i] == '(')
//                 l++;
//             else if (s[i] == ')') {
//                 if (l > 0)
//                     l--;
//                 else
//                     r++;
//             }
//         }

//         boolean[] isDelete = new boolean[s.length];
//         ArrayList<boolean[]> list = new ArrayList<>();
//         ArrayList<int[]> poslrlist = new ArrayList<>();
//         list.add(isDelete);
//         poslrlist.add(new int[] { 0, l, r });

//         boolean find = false;
//         while (!find) {
//             ArrayList<boolean[]> next = new ArrayList<>();
//             ArrayList<int[]> nextposlr = new ArrayList<>();
//             for (int k = 0; k < list.size(); k++) {
//                 boolean[] curStat = list.get(k);
//                 int[] poslr = poslrlist.get(k);
//                 l = poslr[1];
//                 r = poslr[2];
//                 if (l == 0 && r == 0 && isValid(curStat, s)) {
//                     StringBuilder news = new StringBuilder();
//                     for (int i = 0; i < curStat.length; i++) {
//                         if (curStat[i] == false)
//                             news.append(s[i]);
//                     }
//                     res.add(news.toString());
//                     find = true;
//                 }

//                 if (!find) {
//                     int pos = poslr[0];
//                     for (int i = pos; i < curStat.length; i++) {
//                         if (i > pos && s[i] == s[i - 1] && curStat[i - 1] == false) {
//                             continue;
//                         }
//                         if (s[i] == ')' && r > 0) {
//                             boolean[] newStat = Arrays.copyOf(curStat, curStat.length);
//                             newStat[i] = true;
//                             next.add(newStat);
//                             nextposlr.add(new int[] { i, l, r - 1 });
//                         } else if (s[i] == '(' && l > 0) {
//                             boolean[] newStat = Arrays.copyOf(curStat, curStat.length);
//                             newStat[i] = true;
//                             next.add(newStat);
//                             nextposlr.add(new int[] { i, l - 1, r });
//                         }
//                     }
//                 }
//             }
//             list = next;
//             poslrlist = nextposlr;
//         }
//         return res;
//     }
// }