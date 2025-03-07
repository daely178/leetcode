# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
 
        slow, fast = head, head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse 2nd half
        curr = slow.next
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        slow.next = None # split 1st half
        first, second = head, prev        

        while first and second:
            nxt1 = first.next # 1,2
            nxt2 = second.next # 4,3

            # 1,2,3,4
            # 1,4,2,3
            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2

'''
    1,2,3,4,5,6
    1,6,2,5,3,4

    first half
    reverse half
    
'''            