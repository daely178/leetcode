# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        pre = dummy
        cur = head

        # 1 <= left <= right <= n
        # # of left
        for i in range(1,left):
            pre = pre.next # left - 1
            cur = cur.next # left

       #  l.  r
       #1,2,3,4,5
       #p c n     <-- refer
       #p n c     <-- assign
        for i in range(right-left): # 0 - (right-left)
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        
        return dummy.next
'''
    left, right = posision    

    list -> left
    1,2,3,4,5
    p
      c
    
    loop (right - left)

head = [1,2,3,4,5], left = 2, right = 4

         l.  r
       1,2,3,4,5
       p c n     <-- refer
       p n c     <-- assign
                            1
    nxt = c.next.          nxt=3
    c.next = nxt.next.     c.next = 4
    nxt.next = pre.next.   nxt.next = 2
    pre.next = nxt         pre.next = 3

'''        