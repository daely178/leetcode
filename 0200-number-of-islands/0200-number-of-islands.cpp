class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int islands=0;
        for(int i=0; i<grid.size(); i++) {
            for(int j=0; j<grid[0].size(); j++){
                if(grid[i][j] == '1') {
                    dfs(i,j,grid);
                    islands++;
                }
            }
        }
        return islands;
    }

    void dfs(int r, int c, vector<vector<char>>&grid) {
        if(r<0 || r>=grid.size() || c <0 || c>=grid[0].size() || grid[r][c]!='1')
            return;
        grid[r][c] = 'x';
        dfs(r+1, c, grid);
        dfs(r-1, c, grid);
        dfs(r, c+1, grid);
        dfs(r, c-1, grid);
    }
};

/*
    looping and find the '1'
    search connected 1's and mark 'x' not to visit again
    make sure not to visit out of index
    increase counter if there is no more
*/