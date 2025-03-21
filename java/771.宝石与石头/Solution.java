import java.util.HashSet;
import java.util.Set;

class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> jewels = new HashSet<Character>();
        for (int i = 0; i < J.length(); i++) {
            jewels.add(J.charAt(i));
        }
        int count = 0;
        for (int i = 0; i < S.length(); i++) {
            if (jewels.contains(S.charAt(i))){
                count++;
            }
        }
        return count;
    }
}

