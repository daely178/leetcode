class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
        int left,right,up,down;
        vector<int> res;

        left = 0;
        right = matrix[0].size()-1;
        up = 0;
        down = matrix.size()-1;

        while(left<=right && up<=down) {
            int i=0;

            i=left;
            while(i<=right) {
                res.push_back(matrix[up][i++]);
            }
            i=++up;
            if(up>down) {
                break;
            }
            while(i<=down) {
                res.push_back(matrix[i++][right]);
            }
            i=--right;
            if(left>right) {
                break;
            }
            while(i>=left) {
                res.push_back(matrix[down][i--]);
            }
            i=--down;
            if(up>down) {
                break;
            }
            while(i>=up) {
                res.push_back(matrix[i--][left]);
            }
            left++;
        }

        return res;
    }
};

/*

 right - down 
  |       |
  up   - left

right - right max && visited
down - bottom max && visited
left - left min && visited
up - up min && visited



*/