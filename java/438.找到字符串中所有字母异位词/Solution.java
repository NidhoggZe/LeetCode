import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        char[] ss = s.toCharArray(), pp = p.toCharArray();
        List<Integer> res = new ArrayList<>();
        if (ss.length < pp.length)
            return res;

        HashMap<Character, Integer> map = new HashMap<>();
        int need = 0;
        for (int i = 0; i < pp.length; i++) {
            map.put(pp[i], map.getOrDefault(pp[i], 0) + 1);
            need++;
        }

        for (int i = 0; i < pp.length; i++) {
            if (map.containsKey(ss[i])) {
                int cur = map.get(ss[i]);
                map.put(ss[i], cur - 1);
                if (cur > 0) {
                    need--;
                }
            }
        }
        if (need == 0)
            res.add(0);


        for (int i = 1; i < ss.length - pp.length + 1; i++) {
            if (map.containsKey(ss[i-1])) {
                int curneed = map.get(ss[i-1]) + 1;
                map.put(ss[i-1], curneed);
                if (curneed > 0) {
                    need++;
                }
            }
            if (map.containsKey(ss[i + pp.length - 1])) {
                int curneed = map.get(ss[i + pp.length - 1]) - 1;
                map.put(ss[i], curneed - 1);
                if (curneed >= 0) {
                    need--;
                }
            }
            if (need == 0) res.add(i);
        }

        return res;
    }
}