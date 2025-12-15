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
        int sz=0;
        ListNode dummy(0);
        dummy.next = head;
        ListNode * tmp = head;
        while(tmp) {
            tmp = tmp->next;
            sz++;
        }
        tmp = &dummy;
        sz -= n;
        while(sz) {
            tmp = tmp->next;
            sz--;
        }
        if(tmp->next)
        {
            tmp->next = tmp->next->next;
        }
        return dummy.next;
    }
};


/*
brute force

jump to nth - 1 node

nth-1 node 0=-> next->next = nth -> next

*/