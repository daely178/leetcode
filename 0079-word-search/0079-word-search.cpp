class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(word.size() ==0){
            return true;
        }
        if(board.size()==0){
            return false;
        }
        for(int i=0; i<board.size(); i++){
            for(int j=0; j<board[0].size(); j++){
                if(board[i][j] == word[0]){
                    if(dfs(i,j,0,board,word)){
                        return true;
                    }
                }
            }
        }
        return false;
    }
    bool dfs(int r, int c, int idx, vector<vector<char>>& board, string word){
        if(idx == word.size()) {
            return true;
        }
        if(r>=board.size() || r<0 || c>=board[0].size() || c<0 || word[idx]!=board[r][c]) 
        {
            return false;
        }
        char temp = board[r][c];
        board[r][c] = '#';
        
        bool found = dfs(r+1,c,idx+1,board,word)||
                     dfs(r-1,c,idx+1,board,word)||
                     dfs(r,c+1,idx+1,board,word)||
                     dfs(r,c-1,idx+1,board,word);
        board[r][c] = temp;
        return found;
    }
};