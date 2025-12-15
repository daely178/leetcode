class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        for(int i=0; i<n; i++) {
            // not i==j
            for(int j=i+1; j<n; j++) {
                swap(matrix[j][i], matrix[i][j]);
                // i=0,j=1 2<->4
                // i=0,j=2 3<->7

                // i=1,j=2 6<->8
            }
        }

        for(int i=0; i<n; i++) {
            for(int j=0; j<n/2; j++) {
                // reverse row
                swap(matrix[i][j], matrix[i][n-j-1]);
            }
        }
    }
};

/*
2D rotate 90 degree in-place memory

[1,2,3], 0,0 0,1 0,2
[4,5,6], 1,0 1,1 1,2
[7,8,9]. 2,0 2,1 2,2

transpose
[1,4,7], 0,0 1,0 2,0
[2,5,8], 0,1 1,1 2,1
[3,6,9]. 0,2 1,2 2,2

reverse

[7,4,1], 2,0 1,0 0,0
[8,5,2], 2,1 1,1 0,1
[9,6,3]  2,2 1,2 0,2


*/