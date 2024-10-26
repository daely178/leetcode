# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        vals = []
        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next
        vals.sort()
        dummy = ListNode()
        tmp = dummy
        for val in vals:
            tmp.next = ListNode(val)
            tmp = tmp.next
        return dummy.next
        
        

# key points
# 1. merge k linked-lists
# 2. 0 <= lists[i].length <= 500
# 3. 0 <= k <= 104
# The sum of lists[i].length will not exceed 104.

# 1. get length
# 2. get first value from first node of all lists
# 3. compare all first values and list up