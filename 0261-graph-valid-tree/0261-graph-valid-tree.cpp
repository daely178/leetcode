class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n-1) return false;

        vector<vector<int>> dag(n);

        for(auto &edge : edges) {
            int e = edge[0], v = edge[1];
            dag[e].push_back(v);
            dag[v].push_back(e);
        }
        unordered_set<int> explored;
        dfs(0, dag, explored);
        return explored.size() == n;
    }
    void dfs(int cur, const vector<vector<int>> &dag, unordered_set<int> &explored) {
        if(explored.count(cur)) return;
        explored.insert(cur);

        for(int adj : dag[cur]) {
            dfs(adj, dag, explored);
        }
    }
};