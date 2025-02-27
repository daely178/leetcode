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
    bool isBalanced(TreeNode* root) {
        if(!root)
            return true;
        
        std::stack<pair<TreeNode*, bool>> st;
        st.push({root, false});

        std::unordered_map<TreeNode*, int> heights;

        while(!st.empty()){
            auto [node, visited] = st.top();
            st.pop();
            if(visited){
                auto leftheight = node->left ? heights[node->left] : 0;
                auto rightheight = node->right ? heights[node->right] : 0;
                if(std::abs(leftheight-rightheight) > 1)
                    return false;
                heights[node] = std::max(leftheight,rightheight)+1;
            }
            else {
                st.push({node, true});
                if(node->left)
                    st.push({node->left, false});
                if(node->right)
                    st.push({node->right, false});
            }
        } 
        return true;
    }
};