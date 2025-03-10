class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if(edges.size() != n-1) return false;
        vector<vector<int>> adjList(n);
        for(auto e : edges) {
            adjList[e[0]].push_back(e[1]);
            adjList[e[1]].push_back(e[0]);
        }
        vector<bool> visited(n, false);
        stack<int> st;
        st.push(0);
        while(!st.empty()) {
            int node = st.top();
            st.pop();
            if(visited[node] == false){
                visited[node] = true;
                for(auto nei : adjList[node]){
                    st.push(nei);
                }
            }
        }
        for(bool v : visited) {
            if(!v) return false;
        }
        return true;
    }
};