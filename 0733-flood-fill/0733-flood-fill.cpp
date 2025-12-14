class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        
        if(image[sr][sc] != color) {
            helper(image, sr, sc, image[sr][sc], color);
        }
        return image;
    }

    void helper(vector<vector<int>>& image, int r, int c, int orgColor, int newColor) {
        if(r>=image.size() || r<0 || c>=image[0].size() || c<0 || image[r][c] != orgColor)
            return;
        
        image[r][c] = newColor;

        helper(image, r+1, c, orgColor, newColor);
        helper(image, r-1, c, orgColor, newColor);
        helper(image, r, c+1, orgColor, newColor);
        helper(image, r, c-1, orgColor, newColor);
    }
};

/*
2D image
change color from starting pixel
directly adjacent that are same color as starting pixel
if horizontally or vertically connect, then diagonal can be changed

[[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

*/