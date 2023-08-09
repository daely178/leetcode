
'''
138. Copy List with Random Pointer
Medium
11.8K
1.2K
Companies
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
'''
class Node:
    head = None
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        dict={}
        temp=head
        if head is None:
            return None
        while temp:
            dict[temp]=Node(temp.val)
            temp=temp.next
        temp=head
        while temp:
            copied=dict[temp]
            if temp.next:
                copied.next=dict[temp.next]
            if temp.random:
                copied.random=dict[temp.random]
            temp=temp.next
        return dict[head]
            
class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # --------------------------------------------------------
        
        # Create mirror node for each node in linked list
        
        cur = head
        
        while cur:
            
            # backup original next node of input linkied list
            original_next_hop = cur.next
            
            # create mirror node with original order
            cur.next = Node( x = cur.val, next = original_next_hop, random = None)
            
            # move to next position
            cur = original_next_hop
        
        
        # --------------------------------------------------------
        
        # Let mirror node get the random pointer
        
        cur = head
        
        while cur:
            
            if cur.random:
                # assign random pointer to mirror node
                cur.next.random = cur.random.next
                
            try:
                # move to next position
                cur = cur.next.next
            except AttributeError:
                break
                
        
        # --------------------------------------------------------
                
        # Separate copy linked list from original linked list
        
        try:
            # locate the head node of copy linked list
            head_of_copy_list = head.next
            cur = head_of_copy_list
            
        except AttributeError:
            # original input is an empty linked list
            return None
        
        while cur:
            
            try:
                # link mirror node to copy linked list
                cur.next = cur.next.next
            except AttributeError:
                break
            
            # move to next position
            cur = cur.next
            
        return head_of_copy_list
    
    def print_linked_list( self, node ):
        
        cur = node
        
        while cur:
            print( f' val = {cur.val} ')
            
            if cur.next:
                print( f' next = {cur.next.val} ')
            else:
                print( f' next = None ')
                
            if cur.random:
                print( f' random = {cur.random.val} ')
            else:
                print( f' random = None')
                
            print( '\n => \n' )
            
            cur = cur.next
            
s = Solution(head = [[7,None],[13,0],[11,4],[10,2],[1,0]])

head = s.copyRandomList()

s.print_linked_list(head)