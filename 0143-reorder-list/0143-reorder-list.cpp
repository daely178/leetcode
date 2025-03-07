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
    void reorderList(ListNode* head) {
        // find mid
        ListNode *slow=head, *fast=head;
        while(fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // reverse 2nd half
        ListNode *prev=nullptr, *next;
        ListNode *curr=slow;
        while(curr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }        

        // mix
        ListNode* first = head;
        ListNode* second = prev;
        while(second->next) {
            ListNode* tmp = first->next;
            first->next = second;
            first = tmp;
            tmp = second->next;
            second->next = first;
            second = tmp;
        }
    }
};