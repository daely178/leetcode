# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        slow, fast = head,head
        for i in range(n):
            fast = fast.next
            if not fast: # only one element
                return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
            
'''
    1,2,3,4,5
    1 -> remove 5

    first = 2


'''            