class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int LEFT=0, RIGHT=matrix[0].size()-1;
        int UP=0, DOWN=matrix.size()-1;
        vector<int> res;

        while(LEFT<=RIGHT && UP<=DOWN) {
            int i=0;
            // go RIGHT
            i=LEFT;
            while(i<=RIGHT){
                res.push_back(matrix[UP][i++]); // 1,2 // UP = 1
            }            
            UP++;
            if(UP > DOWN)
                break;

            // go DOWN
            i=UP;
            while(i<=DOWN){
                res.push_back(matrix[i++][RIGHT]);
            }
            --RIGHT;            
            if(LEFT > RIGHT)
                break;

            // go LEFT
            i=RIGHT;
            while(i>=LEFT){
                res.push_back(matrix[DOWN][i--]);
            }
            --DOWN;
            if(UP > DOWN)
                break;
            // go UP
            i=DOWN;
            while(i>=UP){
                res.push_back(matrix[i--][LEFT]);
            }            
            LEFT++;
        }

        return res;
    }
};

/*
    RIGHT DOWN LEFT UP

    for()
*/