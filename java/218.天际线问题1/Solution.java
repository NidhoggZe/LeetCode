import java.util.List;
import java.util.TreeMap;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        int[][] points = new int[buildings.length * 2][];
        int count = 0;
        List<List<Integer>> res = new ArrayList<>();
        for (int[] building : buildings) {
            points[count++] = new int[] { building[0], -building[2] };
            points[count++] = new int[] { building[1], building[2] };
        }
        TreeMap<Integer, Integer> map = new TreeMap<>();
        map.put(0, 1);

        Arrays.sort(points, new Comparator<int[]>() {
            @Override
            public int compare(int[] p1, int[] p2) {
                if (p1[0] != p2[0])
                    return p1[0] - p2[0];
                else
                    return p1[1] - p2[1];
            }
        });

        for (int[] p : points) {
            int lasth = map.lastKey();
            if (p[1] < 0)
                map.put(-p[1], map.getOrDefault(-p[1], 0) + 1);
            else
                if (map.get(p[1]) == 1) map.remove(p[1]);
                else map.put(p[1], map.get(p[1]) - 1);

            if (lasth != map.lastKey()) {
                ArrayList<Integer> temp = new ArrayList<>();
                temp.add(p[0]);
                temp.add(map.lastKey());
                res.add(temp);
            }
        }

        return res;
    }
}