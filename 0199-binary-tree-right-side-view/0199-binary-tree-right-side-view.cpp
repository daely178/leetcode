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
    vector<int> rightSideView(TreeNode* root) {
        if(!root) return vector<int>();

        deque<TreeNode*> q{root};
        vector<int> rightside;

        while(!q.empty()){
            int level_len = q.size();

            for(int i=0; i<level_len; i++){
                TreeNode* node = q.front();
                q.pop_front();
                if(i==level_len-1)
                    rightside.push_back(node->val);
                if(node->left)
                    q.push_back(node->left);
                if(node->right)
                    q.push_back(node->right);
            }
        }
        return rightside;
    }
};