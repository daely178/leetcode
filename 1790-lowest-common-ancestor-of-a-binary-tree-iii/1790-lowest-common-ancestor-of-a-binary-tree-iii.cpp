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
        if (p==q){
            return p;
        }

        int pd=0, qd=0;
        Node *temp = p;
        while(temp) {
            temp=temp->parent;
            pd++;
        }
        temp = q;
        while(temp){
            temp = temp->parent;
            qd++;
        }
        if(pd > qd){
            int i=0, diff = pd-qd;
            while(i<diff) {
                p = p->parent;
                i++;
            }
        } else {
            int i=0, diff = qd-pd;
            while(i<diff) {
                q = q->parent;
                i++;
            }
        }

        while(p!=q){
            p = p->parent;
            q = q->parent;
        }
        return p;
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