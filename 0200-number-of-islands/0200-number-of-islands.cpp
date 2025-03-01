class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        int nc = grid[0].size();  
        int res = 0; 

        for(int r=0; r<nr; r++){
            for(int c=0; c<nc; c++) {
                if(grid[r][c] == '1') {
                    dfs(grid, r,c);
                    res+=1;
                }
            }
        }
        return res;
    }

    void dfs(vector<vector<char>>& grid, int r, int c) {
        int nr = grid.size();
        int nc = grid[0].size(); 

        if(r>=nr || r<0 || c>=nc || c<0 || grid[r][c] != '1')
        {
            return;
        }
        grid[r][c] = 'x';
        dfs(grid, r+1, c);
        dfs(grid, r-1, c);
        dfs(grid, r, c+1);
        dfs(grid, r, c-1);
    }
};