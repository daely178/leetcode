/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* cloneGraph(Node* node) {
        queue<Node*> q;
        unordered_map<Node*, Node*> visited;

        if(!node) {
            return node;
        }
        visited[node] = new Node(node->val, {});
        q.push(node);
        while(!q.empty()) {
            Node *n = q.front();
            q.pop();
            for(Node *v : n->neighbors){
                if(visited.find(v) == visited.end()){
                    visited[v] = new Node(v->val, {});
                    q.push(v);
                }
                visited[n]->neighbors.push_back(visited[v]);
            }
        }
        return visited[node];
    }
};