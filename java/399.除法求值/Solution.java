import java.util.List;
import java.util.HashMap;

//带权并查集
class Solution {

    int refresh(int[] parent, double[] lengthToParent, int x) {
        int root = x;
        double length = 1.0;
        while (parent[root] != root) {
            length *= lengthToParent[root];
            root = parent[root];
        }
        while (parent[x] != root) {
            int t = parent[x];
            parent[x] = root;
            length /= lengthToParent[x];
            lengthToParent[x] *= length;
            x = t;
        }
        return root;
    }

    void union(int[] parent, double[] lengthToParent, int x, int y, double xdivy) {
        int root = refresh(parent, lengthToParent, y);
        parent[root] = x;
        lengthToParent[root] = xdivy/lengthToParent[y];
        refresh(parent, lengthToParent, y);
    }

    double distance(int[] parent, double[] lengthToParent, int x, int y) {
        if (x == y)
            return 1.0;
        double lengthx = 1.0, lengthy = 1.0;
        while (parent[x] != x) {
            lengthx *= lengthToParent[x];
            x = parent[x];            
        }
        while (parent[y] != y) {
            lengthy *= lengthToParent[y];
            y = parent[y];
        }
        if (x != y) return -1.0;
        return lengthy/lengthx;
    }

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        HashMap<String, Integer> toint = new HashMap<>();
        int count = 0;
        for (List<String> pair : equations) {
            String word1 = pair.get(0), word2 = pair.get(1);
            if (!toint.containsKey(word1)) {
                toint.put(word1, count);
                count++;
            }
            if (!toint.containsKey(word2)) {
                toint.put(word2, count);
                count++;
            }
        }

        double[] lengthToParent = new double[count];
        int[] parent = new int[count];
        for (int i = 0; i < count; i++) {
            lengthToParent[i] = 1.0;
            parent[i] = i;
        }
        count = 0;
        for (List<String> pair : equations) {
            int idx1 = toint.get(pair.get(0)), idx2 = toint.get(pair.get(1));
            union(parent, lengthToParent, idx1, idx2, values[count]);
            count++;
        }

        double[] res = new double[queries.size()];
        for (int i = 0; i < res.length; i++) {
            String word1 = queries.get(i).get(0), word2 = queries.get(i).get(1);
            if (!toint.containsKey(word1) || !toint.containsKey(word2)) {
                res[i] = -1.0;
                continue;
            }
            int begin = toint.get(queries.get(i).get(0)), end = toint.get(queries.get(i).get(1));
            res[i] = distance(parent, lengthToParent, begin, end);
        }

        return res;
    }
}