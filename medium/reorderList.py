'''
143. Reorder List
Medium
9.3K
310
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        copiedList = {}

        temp = head
        count = 0
        while temp:
            copiedList[count] = temp
            temp = temp.next
            count += 1

        left = 0
        right = count -1
        if count > 2:
            while left<right:

                forward_node = copiedList[left]
                forward_next_node = copiedList[left+1]
                backward_node = copiedList[right]

                forward_node.next = backward_node
                backward_node.next = forward_next_node
                
                left += 1
                right -= 1
                
            # when left=right which is mid index is the last node after reorder
            forward_node = copiedList[left]
            forward_node.next = None

head = ListNode(0)
temp = head          
for i in range(1, 4, 1):
    node = ListNode(i)
    temp.next = node
    temp = temp.next

s = Solution()
s.reorderList(head.next)

print("done")
