class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n+1, INT_MAX);
        vector<vector<pair<int, int>>> adj(n+1);

        // adjacent list
        for(auto &e : times) {
            adj[e[0]].push_back({e[1], e[2]}); // u, v, w
        }

        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> pq;
        dist[k] = 0;
        pq.push({0,k});

        while(!pq.empty()) {
            auto curr_dist = pq.top().first;
            auto node = pq.top().second;
            pq.pop();
            if(curr_dist > dist[node]) {
                continue;
            }

            for(auto &e : adj[node]) {
                auto v = e.first;
                auto w = e.second;
                if(dist[node]+w < dist[v]) {
                    dist[v] = dist[node]+w;
                    pq.push({dist[v], v});
                }
            }
        }
        int ans = INT_MIN;
        for(int i=1; i<=n; i++) {
            ans = max(dist[i], ans);
        }

        return ans == INT_MAX ? -1 : ans;
    }
};

/*

adjacent list
 u : v, w
dist(n+1, INT_MAX)
priority queue <dist1,node1> <dist2,node2> big to small
add starting point
pq.push_back({0, k})
while(pq) {
    node = pq.top().second
    curr_dist = pq.top().first
    pq.pop()

    if(dist[node] < curr_dist ) {
        continue // no need to visit if weight is expensive
    }
    for(auto &e : adj[node]) {}
}
*/