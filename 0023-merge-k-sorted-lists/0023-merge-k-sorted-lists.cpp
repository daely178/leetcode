/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> vals;
        for(auto l : lists) {
            ListNode *t = l;
            while(t){
                vals.push_back(t->val);
                t = t->next;
            }            
        }
        sort(vals.begin(), vals.end());
        ListNode dummy(-1);
        ListNode *temp = &dummy;

        for(auto v : vals) {
            temp->next = new ListNode(v);
            temp = temp->next;
        }
        return dummy.next;
    }
};