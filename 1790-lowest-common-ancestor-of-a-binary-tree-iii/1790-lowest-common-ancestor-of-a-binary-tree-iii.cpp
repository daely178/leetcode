/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* parent;
};
*/

class Solution {
public:
    Node* lowestCommonAncestor(Node* p, Node * q) {
        Node* a = p;
        Node* b = q;
        while(a != b) {
            a = a == nullptr ? q : a->parent;
            b = b == nullptr ? p : b->parent;  
        }
        return b;        
    }
};

// 4 2 5 3 N 0 1 3 N
// 0 1 3 N 4 2 5 3 N