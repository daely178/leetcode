'''
846. Hand of Straights
Solved
Medium
Topics
Companies
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length
 '''
 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        hmap = defaultdict(int)
        for num in hand:
            hmap[num] += 1
        
        hand.sort()

        for i in range(len(hand)):

            if hmap[hand[i]] == 0:
                continue
            for k in range(groupSize):
                if hmap[hand[i]+k] == 0:
                    return False                
                hmap[hand[i]+k] -= 1

        return True

class Solution2:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize != 0:
            return False

        hq = []
        for num in hand:
            heapq.heappush(hq, num)

        prev = -1
        count = 0
        tmp = []
        
        while hq:
            curr = heapq.heappop(hq)
            
            if (curr - prev) == 1 or prev == -1:
                count += 1
                prev = curr
            else:
                heapq.heappush(tmp, curr)
            
            if count == groupSize:
                count = 0
                prev = -1
                for e in tmp:
                    heapq.heappush(hq, e)
                tmp = []
        
        if count:
            return False
        return True


 
'''
hand = [1,2,3,6,2,3,4,7,8], groupSize = 3

sort = 1,2,2,3,3,4,6,7,8

    3. 1 1+1 1+2

ht  = [1:1, 2:2, 3:2, 6:1, 4:1, 7:1, 8:1]
pq = [ 1,2,2,3,3,4,6,7,8]

1,2,3,1,2,3


'''        