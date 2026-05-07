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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        std::queue<TreeNode*> queue;
        if(!root) {
            return {};
        }

        queue.push(root);
        while(!queue.empty()) {
            vector<int> curr;
            int n = queue.size();
            for(int i=0; i<n; i++) {
                TreeNode *node = queue.front();
                curr.push_back(node->val);
                queue.pop();
                if(node->left) queue.push(node->left);
                if(node->right) queue.push(node->right);
            }
            levels.push_back(curr);
        }

        return levels;
    }
};

/*
stack FIFO
queue LIFO
add node
add left right

*/