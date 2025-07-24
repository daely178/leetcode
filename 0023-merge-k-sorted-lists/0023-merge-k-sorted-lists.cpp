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
        std::vector<int> vals;
        
        for(auto ls : lists) {
            ListNode* sub = ls;
            while(sub){
                vals.push_back(sub->val);
                sub = sub->next;
            }
        }

        sort(vals.begin(), vals.end());
        ListNode dummy;
        ListNode *tmp = &dummy;
        for(auto val : vals) {
            tmp->next = new ListNode(val);
            tmp = tmp->next;
        }
        return dummy.next;
    }
};