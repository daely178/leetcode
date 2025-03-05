class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int rows = matrix.size();
        int cols = matrix[0].size();
        int up=0, left=0, right=cols-1, down=rows-1;

        while(ans.size() < rows*cols) {
            for(int col=left; col<=right; col++){
                ans.push_back(matrix[up][col]);
            }
            for(int row=up+1; row<=down; row++) {
                ans.push_back(matrix[row][right]);
            }
            if(up!=down){
                for(int col=right-1; col>=left; col--){
                    ans.push_back(matrix[down][col]);
                }
            }
            if(left!=right){
                for(int row=down-1; row>up; row--){
                    ans.push_back(matrix[row][left]);
                }
            }
            left++;
            right--;
            up++;
            down--;
        }
        return ans;
    }
};