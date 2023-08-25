'''
355. Design Twitter
Medium
3.4K
427
Companies
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
'''

from typing import List
from collections import deque, defaultdict
import heapq, itertools, collections
from queue import PriorityQueue

class Twitter:

    def __init__(self):
        # Use itertools.count to generate a decreasing sequence of integers for tweets
        self.timer = itertools.count(step=-1)
        # Use defaultdict and deque to store tweets for each user
        self.tweets = collections.defaultdict(deque)
        # Use defaultdict and set to store followees for each user
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet to the left of the deque for the user, along with its timestamp
        self.tweets[userId].appendleft((next(self.timer), tweetId))
        # If the deque for the user has more than 10 tweets, remove the oldest tweet from the right
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        # Merge the tweets of the user's followees (including the user) using heapq.merge
        tweets = list(heapq.merge(
        *(self.tweets[followee] for followee in self.followees[userId] | {userId})))
        # Return the tweet IDs of the 10 most recent tweets
        return [tweetId for _, tweetId in tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the set of followees for the follower
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Remove the followee from the set of followees for the follower (if the followee exists)
        self.followees[followerId].discard(followeeId)
        
class TwitterMine:

    def __init__(self):
        self.tweetDB = defaultdict(deque)
        self.followDB = defaultdict(set)
        self.time = -1   

    def postTweet(self, userId: int, tweetId: int) -> None:        
        self.tweetDB[userId].appendleft((self.time, tweetId))
        self.time -= 1
        if len(self.tweetDB[userId]) > 10:
            self.tweetDB[userId].pop() # Maintain 10 after removing oldest one

    def getNewsFeed(self, userId: int) -> List[int]:
        
        totaltweets = []
        totaltweets += self.tweetDB[userId]
        for followee in self.followDB[userId]:
            totaltweets.extend(self.tweetDB[followee])

        heapq.heapify(totaltweets)
        
        ans = []
        while totaltweets and len(ans) <= 10:
            ans.append(heapq.heappop(totaltweets)[1])
            
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followDB[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followDB[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
#Input
#["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
#[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
#Output
#[null, null, [5], null, null, [6, 5], null, [5]]

# ["Twitter",
# "postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet",
# "postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet",
# "postTweet","postTweet","postTweet","postTweet","postTweet","postTweet",
# "getNewsFeed","follow",
# "getNewsFeed","unfollow","getNewsFeed"]
# [[],
# [1,5],[2,3],[1,101],[2,13],[2,10],[1,2],[1,94],[2,505],[1,333],[2,22],[1,11],[1,205],[2,203],[1,201],
# [2,213],[1,200],[2,202],[1,204],[2,208],[2,233],[1,222],[2,211],
# [1],[1,2],[1],[1,2],[1]]

'''
Output
[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
[222,204,200,201,205,11,333,94,2,101],null,[211,222,233,208,204,202,200,213,201,203,205,11,22,333,505,94,2,10,13,101],null,[222,204,200,201,205,11,333,94,2,101]]
Expected
[null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
[222,204,200,201,205,11,333,94,2,101],null,[211,222,233,208,204,202,200,213,201,203],null,[222,204,200,201,205,11,333,94,2,101]]
'''
obj = TwitterMine()
obj.postTweet(1,5)
obj.postTweet(2,3)
obj.postTweet(1,101)
obj.postTweet(2,13)
obj.postTweet(2,10)
obj.postTweet(1,2)
obj.postTweet(1,94)
obj.postTweet(2,505)
obj.postTweet(1,333)
obj.postTweet(2,22)
obj.postTweet(1,11)
obj.postTweet(1,205)
obj.postTweet(2,203)
obj.postTweet(1,201)
obj.postTweet(2,213)
obj.postTweet(1,200)
obj.postTweet(2,202)
obj.postTweet(1,204)
obj.postTweet(2,208)
obj.postTweet(2,233)
obj.postTweet(1,222)
obj.postTweet(2,211)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.follow(1,2)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.unfollow(1,2)
param_2 = obj.getNewsFeed(1)
print(param_2)
#obj.follow(2,1)
#param_2 = obj.getNewsFeed(2)
#obj.unfollow(2,1)
#param_2 = obj.getNewsFeed(2)