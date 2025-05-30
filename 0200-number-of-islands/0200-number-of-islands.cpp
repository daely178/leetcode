class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int numOfIslands = 0;

        for(int i=0; i<grid.size(); i++) {
            for(int j=0; j<grid[0].size(); j++) {
                if(grid[i][j] == '1') {
                    dfs(grid, i,j);
                    numOfIslands++;
                }
            }
        }
        return numOfIslands;
    }

    void dfs(vector<vector<char>> &grid, int i, int j){
        if(i>=grid.size() || i<0 || j>=grid[0].size() || j<0 || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '0';
        dfs(grid, i+1, j);
        dfs(grid, i-1, j);
        dfs(grid, i, j+1);
        dfs(grid, i, j-1);
    }
};