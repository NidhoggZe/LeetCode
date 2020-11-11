import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        StringBuffer str = new StringBuffer();
        Stack<Integer> multiStack = new Stack<>();
        Stack<StringBuffer> ansStack = new Stack<>();
        int multi = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c))
                multi = multi * 10 + c - '0';
            else if (c == '[') {
                ansStack.add(str);
                multiStack.add(multi);
                str = new StringBuffer();
                multi = 0;
            } else if (c == ']') {
                StringBuffer ansTmp = ansStack.pop();
                int mutiTmp = multiStack.pop();
                for (int i = 0; i < mutiTmp; i++)
                    ansTmp.append(str);
                str = ansTmp;
            } else {
                str.append(c);
            } 
        }
        return str.toString();
    }
}