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
        vector<int> val_list;
        for(auto l : lists) {
            ListNode *tmp = l;
            while(tmp) {
                val_list.push_back(tmp->val);
                tmp = tmp->next;
            }
        }

        ListNode head;
        ListNode *tmp = &head;
        sort(val_list.begin(), val_list.end());
        for(auto val : val_list) {
            tmp->next = new ListNode(val);
            tmp = tmp->next;
        }
        return head.next;
    }
};