import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

class Solution {
    ArrayList<int[]> merge(ArrayList<int[]> curGroup1, ArrayList<int[]> curGroup2) {
        ArrayList<int[]> newcurGroup = new ArrayList<>();
        int i = 0, j = 0, h1 = 0, h2 = 0;
        while (i < curGroup1.size() || j < curGroup2.size()) {
            long x1 = i < curGroup1.size() ? curGroup1.get(i)[0] : Long.MAX_VALUE;
            long x2 = j < curGroup2.size() ? curGroup2.get(j)[0] : Long.MAX_VALUE;
            long x;
            if (x1 < x2) {
                h1 = curGroup1.get(i)[1];
                x = x1;
                i++;
            } else if (x1 > x2) {
                h2 = curGroup2.get(j)[1];
                x = x2;
                j++;
            } else {
                h1 = curGroup1.get(i)[1];
                h2 = curGroup2.get(j)[1];
                x = x1;
                i++;
                j++;
            }
            int h = Math.max(h1, h2);
            if (newcurGroup.isEmpty() || newcurGroup.get(newcurGroup.size() - 1)[1] != h)
                newcurGroup.add(new int[] { (int)x, h });
        }
        return newcurGroup;
    }

    public List<List<Integer>> getSkyline(int[][] buildings) {
        if (buildings.length == 0) return new ArrayList<List<Integer>>();
        LinkedList<ArrayList<int[]>> groups = new LinkedList<>();
        for (int[] building : buildings) {
            ArrayList<int[]> curGroup = new ArrayList<>();
            int[] p1 = { building[0], building[2] };
            int[] p2 = { building[1], 0 };
            curGroup.add(p1);
            curGroup.add(p2);
            groups.add(curGroup);
        }

        while (groups.size() > 1) {
            int n = groups.size();
            while (n > 1) {
                ArrayList<int[]> curGroup1 = groups.pollFirst();
                ArrayList<int[]> curGroup2 = groups.pollFirst();
                groups.add(merge(curGroup1, curGroup2));
                n -= 2;
            }
            if (n == 1)
                groups.add(groups.pollFirst());
        }

        ArrayList<List<Integer>> res = new ArrayList<>();

        for (var point : groups.get(0)) {
            ArrayList<Integer> temp = new ArrayList<>();
            temp.add(point[0]);
            temp.add(point[1]);
            res.add(temp);
        }

        return res;

    }
}