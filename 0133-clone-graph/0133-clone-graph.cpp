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

       if(!node) {
        return node;
       }
       queue<Node*> q;
       q.push(node);
       unordered_map<Node*, Node*> visited;
       visited[node] = new Node(node->val, {});

       while(!q.empty()) {
        Node* n = q.front();
        q.pop();
        for(auto neighbor : n->neighbors) {
            if(visited.find(neighbor) == visited.end()) {
                visited[neighbor] = new Node(neighbor->val, {});
                q.push(neighbor);
            }
            // connect newly created one to neighbors
            visited[n]->neighbors.push_back(visited[neighbor]);
        }
       }
       return visited[node];
    }
};

/*
deep copy = create new instances
Node : val, neighbors

The number of nodes in the graph is in the range [0, 100].


1 neighbors 2,3
2 neighbors 1,3
3 neighbors 2,4
4 neighbors 1,3

1 - 2
|.  |
4 - 3

queue to add all node
visited to check visited

*/