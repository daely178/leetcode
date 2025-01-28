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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode *head;
        ListNode *temp = new ListNode();
        int carry = 0;

        head = temp;
        
        while(l1 != NULL || l2 != NULL || carry){
            int val1= l1 ? l1->val : 0;
            int val2= l2 ? l2->val : 0;
            int total = carry + val1 + val2;
            carry = 0;
            if (total > 9){
                carry = 1;
            }
            ListNode *newNode = new ListNode(total%10);
            temp->next = newNode;
            temp = temp->next;
            if(l1 != NULL)
                l1 = l1->next;
            if(l2 != NULL)
                l2 = l2->next;
        }
        temp = head->next;
        delete head;
        return temp;
    }
};