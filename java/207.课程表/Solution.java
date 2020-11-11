class Solution {
    boolean dfs(int course, HashMap<Integer, ArrayList<Integer>> map, int[] exist) {
        if (exist[course] == 2) return true;
        if (exist[course] == 1) return false;
        if (!map.containsKey(course)) return true;
        boolean flag = true;
        for (int prepare : map.get(course)) {
            exist[course] = 1;
            if (!dfs(prepare, map, exist)) {
                flag = false;
                break;
            }
        }
        if (flag == true)
            exist[course] = 2;
        return flag;
    }


    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        for (int[] pair : prerequisites) {
            if (map.containsKey(pair[0])) 
                map.get(pair[0]).add(pair[1]);
            else {
                ArrayList<Integer> lst = new ArrayList<Integer>();
                lst.add(pair[1]);
                map.put(pair[0], lst);
            }
        }

        int[] exist = new int[numCourses];
        for (int i = 0; i < exist.length; i++) {
            exist[i] = 0;
        }
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(i, map, exist))
                return false;
        }
        return true;
    }
}