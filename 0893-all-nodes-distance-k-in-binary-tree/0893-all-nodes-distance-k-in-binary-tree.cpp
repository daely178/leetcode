/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    unordered_map<int, vector<int>> graph;
    unordered_set<int> visited;
    vector<int> res;
    
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
        queue<pair<TreeNode*, TreeNode*>> q;


        q.push({root, NULL});

        while(!q.empty()){
            TreeNode *cur = q.front().first;
            TreeNode *par = q.front().second;
            q.pop();
            if(cur && par){
                graph[cur->val].push_back(par->val);
                graph[par->val].push_back(cur->val);
            }
            if(cur->left) {
                q.push({cur->left, cur});
            }
            if(cur->right){
                q.push({cur->right, cur});
            }
        }

        visited.insert(target->val);
        dfs(target->val, 0, k);

        return res;
    }
    void dfs(int cur, int dist, int K) {
        if(dist == K){
            res.push_back(cur);
        }
        for(int nei : graph[cur]){
            if(visited.find(nei) == visited.end()){
                visited.insert(nei);
                dfs(nei, dist+1, K);
            }
        }
    }
};