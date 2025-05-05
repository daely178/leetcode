/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int getHeight(TreeNode* node) {
        if(node == NULL){
            return 0;
        }
        int left = getHeight(node->left);
        int right = getHeight(node->right);
        
        return max(left,right)+1;
    }
    bool isBalanced(TreeNode* root) {
        if (root == NULL)
            return true;
        int left = getHeight(root->left);
        int right = getHeight(root->right);
        return abs(left-right) <= 1 && isBalanced(root->left) && isBalanced(root->right);
    }
};