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
        Node *a = p;
        Node *b = q;
        while(a!=b) {
            a = a==NULL ? q : a->parent;
            b = b==NULL ? p : b->parent;
        }
        return a;


    }
};
/*
        r
               L
            p       
                  q

    p to r = x
    q to r = y
    L to r = z
    p to q through L = x + y - z
    q to p through L = y + x - z
*/