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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode dummy(-1);
        int length = 0;
        dummy.next = head;
        ListNode *curr = dummy.next;

        while(curr!=NULL){
            length++;
            curr = curr->next;
        }

        length -= n;
        curr = &dummy;
        while(length>0){
            length--;
            curr = curr->next;
        }
        curr->next= curr->next->next;
        return dummy.next;
    }
};