import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

class Solution {

    public int[][] reconstructQueue(int[][] people) {
        Arrays.sort(people, (o1, o2) -> o1[0] == o2[0] ? o1[1] - o2[1] : o2[0] - o1[0]);

        // for (int i = 0; i < people.length; i++) {
        // int count = 0;
        // for (int j = 0; j < i; j++) {
        // if (people[j][0] >= people[i][0])
        // count++;
        // }
        // if (count > people[i][1]) {
        // count -= people[i][1];
        // int pos = i, lastpos = i;
        // while (pos > 0 && count > 0) {
        // pos--;
        // if (people[pos][0] >= people[lastpos][0]) {
        // int[] t = people[pos];
        // people[pos] = people[lastpos];
        // people[lastpos] = t;
        // lastpos = pos;
        // count--;
        // }
        // }
        // }
        // }
        List<int[]> list = new LinkedList<>();
        for (int[] arr : people) {
            list.add(arr[1], arr);
        }
        return list.toArray(new int[people.length][2]);

    }
}