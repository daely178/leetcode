class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int islands = 0;

        for(int r=0; r<rows; r++) {
            for(int c=0; c<cols; c++) {
                if(grid[r][c] == '1') {
                    dfs(grid, r, c, rows, cols);
                    islands++;
                }
            }
        }
        return islands;
    }
    void dfs(vector<vector<char>>& grid, int r, int c, int rows, int cols) {
        if(c<cols && r<rows && c>=0 && r>=0 && grid[r][c]=='1') {
            grid[r][c] = 'x';
            dfs(grid, r+1, c, rows, cols);
            dfs(grid, r-1, c, rows, cols);
            dfs(grid, r, c+1, rows, cols);
            dfs(grid, r, c-1, rows, cols);
        }
    }
};

/*

search all corners and replace 1 with other char to show visited
until helper returns

dfs
if "1"
    dfs left,right,up,down and mark "x" for visited


*/