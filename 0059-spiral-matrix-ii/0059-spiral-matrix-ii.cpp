class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {

        int left,right,up,down;
        int count = 1;
        vector<vector<int>> res(n, vector<int>(n));

        left = 0;
        right = n-1;
        up = 0;
        down = n-1;

        while(left<=right && up<=down) {
            for(int j=left; j<=right; j++) res[up][j] = count++;
            if(++up > down) break;
            
            for(int i=up; i<=down; i++) res[i][right] = count++;
            if(--right<left) break;

            for(int j=right; j>=left; j--) res[down][j] = count++;        
            if(--down<up) break;

            for(int i=down; i>=up; i--) res[i][left] = count++;
            left++;
        }
        return res;
    }
};


/*

 0,0    ->. 0,n-1 

  |          |
 n-1,0 <-   n-1,n-1



*/