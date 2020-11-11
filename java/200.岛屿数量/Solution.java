class Solution {
    void isValid(int y, int x, int row, int col, char[][] grid, Queue<Integer> queue) {
        if (x < 0 || y < 0 || x >= col || y >= row || grid[y][x] == '0')
            return;
        else {
            grid[y][x] = '0';
            queue.offer(y * col + x);
            return;
        }
    }

    public int numIslands(char[][] grid) {
        if (grid.length == 0) return 0;
        Queue<Integer> queue = new LinkedList<Integer>();
        int row = grid.length, col = grid[0].length;
        int count = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    grid[i][j] = '0';
                    queue.offer(i * col + j);
                    while (!queue.isEmpty()) {
                        int point = queue.poll(), oldx = point % col, oldy = point / col;
                        isValid(oldy - 1, oldx, row, col, grid, queue);
                        isValid(oldy + 1, oldx, row, col, grid, queue);
                        isValid(oldy, oldx - 1, row, col, grid, queue);
                        isValid(oldy, oldx + 1, row, col, grid, queue);
                    }
                }
            }
        }
        return count;

    }
}