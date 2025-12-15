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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy;
        ListNode *tmp = &dummy;

        ListNode* l1 = list1;
        ListNode* l2 = list2;

        while(l1 && l2) {
            if(l1->val < l2->val) {
                tmp->next = l1;
                l1 = l1->next;
            } else {
                tmp->next = l2;
                l2 = l2->next;
            }
            tmp = tmp->next;
        }
        while(l1) {
            tmp->next = l1;
            l1=l1->next;
            tmp = tmp->next;
        }
        while(l2) {
            tmp->next = l2;
            l2 = l2->next;
            tmp = tmp->next;
        }

        return dummy.next;
    }
};

/*

dummy

while(l1 && l2) 
    if l1.val < l2.val
        dummy.next = l1
        l1 = l1.next
    else
        dummy.next = l2
        l2 = l2.next

while(l1)
    dummy.next = l1
    l1 = l1.next
while(l2)
    dummy.next = l2
    le = l2.next

*/