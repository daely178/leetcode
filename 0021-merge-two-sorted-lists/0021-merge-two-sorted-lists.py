# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        ans = dummy
        while list1 and list2:
            if list1.val > list2.val:
                ans.next = list2
                list2 = list2.next
            else:
                ans.next = list1
                list1 = list1.next
            ans = ans.next
        if list1:
            ans.next = list1
        else:
            ans.next = list2
        return dummy.next


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        else:
            dummy.next = list2
        return head.next
             
'''
    list1 = [1,2,4], list2 = [1,3,4]

    list1 = 
    list2
'''        