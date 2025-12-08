class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int islands = 0;
        for(int i=0; i<grid.size(); i++) {
            for(int j=0; j<grid[0].size(); j++) {
                if(grid[i][j] == '1'){
                    helper(grid, i,j);
                    islands++;
                }
            }
        }
        return islands;
    }

    void helper(vector<vector<char>>& grid, int r, int c){
        if(r>=grid.size() || r<0 || c >= grid[0].size() || c < 0 || grid[r][c] != '1') {
            return;
        }
        grid[r][c]='x';
        helper(grid, r, c+1);
        helper(grid, r, c-1);
        helper(grid, r+1, c);
        helper(grid, r-1, c);
    }
};

/*

search all corners and replace 1 with other char to show visited
until helper returns

*/