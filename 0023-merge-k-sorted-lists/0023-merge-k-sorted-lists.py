# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        vals = []
        head = ListNode()
        dummy = head
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        vals.sort()
        for val in vals:
            dummy.next = ListNode(val)
            dummy = dummy.next

        return head.next
        
        

# key points
# 1. merge k linked-lists
# 2. 0 <= lists[i].length <= 500
# 3. 0 <= k <= 104
# The sum of lists[i].length will not exceed 104.

# 1. get length
# 2. get first value from first node of all lists
# 3. compare all first values and list up