'''
206. Reverse Linked List
Easy
19.1K
347
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 1, 2, 3, 4, 5
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

            # 1.next = None
            # 2.next = 1
            # 3.next = 2
            # 4.next = 3
            # 5.next = 4

        return prev

        
s = Solution()

LOOP_CNT = 6

head = ListNode(0)
temp = head          
for i in range(1, LOOP_CNT, 1):
    node = ListNode(i)
    temp.next = node
    temp = temp.next

result = s.reverseList(head.next)
temp = result
for i in range(1, LOOP_CNT, 1):
    print("{}, ".format(temp.val))
    temp = temp.next