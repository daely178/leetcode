'''
25. Reverse Nodes in k-Group
Hard
12.1K
605
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.


Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 5000
0 <= Node.val <= 1000
'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class SolutionBruteForce:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if k == 1:
            return head
        
        temp = head
        count = 0
        table = {}
        while temp:
            table[count] = temp
            count += 1
            temp = temp.next

        if count < k:
            return head

        section_cnt = 1 # divide by k number of section
        total_run = count//k # Do not touch less than k number of nodes at the end
        head = table[k*section_cnt-1]
        first_node, last_node = head, None
        
        # Time complexity : O(n) = section_cnt * number of nodes in each section
        # Space complexity : 0(n)
        while section_cnt <= total_run: # start from 1

            # 1,2,3,4,5
            # 2,1,4,3,5
            
            # link null->2, 1->4, 3->5
            # if count == k, 1->null
            # sections : [first - next nodes - last], [first - next nodes - last] .... remaining
            
            first_node = table[k*section_cnt-1]
            if last_node:
                last_node.next = first_node

            # reverse nodes in section
            # 2->1, 4->3
            for i in range(k*section_cnt-2, k*(section_cnt-1)-1, -1):
                first_node.next = table[i]
                first_node = first_node.next
                
            last_node = first_node    
            section_cnt += 1
            
        if count == k or count%k==0:
            last_node.next = None
        else:
            last_node.next = table[k*(section_cnt-1)]
            
        return head
    
# Must understand Leetcode 206. Reverse Linked List
# Reduce space complexity

class SolutionOptimize2:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        # verify current section length is equal to k
        for _ in range(k):
            if not curr: return head
            curr = curr.next
        prev = None
        curr = head
        # run first section before recursion
        for _ in range(k): # same as leetcode 206
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head.next = self.reverseKGroup(curr, k)
        return prev # prev = last node after reverse
    
s = SolutionOptimize2()

LOOP_CNT = 6

head = ListNode(0)
temp = head          
for i in range(1, LOOP_CNT, 1):
    node = ListNode(i)
    temp.next = node
    temp = temp.next

result = s.reverseKGroup(head.next, k = 2)
temp = result
for i in range(1, LOOP_CNT, 1):
    print("{}, ".format(temp.val))
    temp = temp.next

# key points
# 1. reverse the nodes of the list k at a time
# 2. 1 <= k <= n <= 5000
# 3. do not touch remaining less number of nodes than k at the end

# Strategy
# 1. With dictionary
# 1-1. Record all in dictionary
# 1-2. Divide section by k size
# 1-3. link first node of section with last node of prev section 




