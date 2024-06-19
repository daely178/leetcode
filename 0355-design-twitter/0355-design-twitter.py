class Twitter:

    def __init__(self):
        self.tweetDB = defaultdict(deque)
        self.followDB = defaultdict(set)
        self.time = 1   

    def postTweet(self, userId: int, tweetId: int) -> None:        
        self.tweetDB[userId].append((self.time, tweetId))
        self.time += 1
        if len(self.tweetDB[userId]) > 10:
            self.tweetDB[userId].popleft() # Maintain 10 after removing oldest one

    def getNewsFeed(self, userId: int) -> List[int]:
        
        totaltweets = []
        #totaltweets += self.tweetDB[userId]
        for tweet in self.tweetDB[userId]:
            heapq.heappush(totaltweets, tweet)
        for followee in self.followDB[userId]:
            for tweet in self.tweetDB[followee]:
                heapq.heappush(totaltweets, tweet)
                if len(totaltweets) > 10:
                    heapq.heappop(totaltweets)
            #totaltweets += self.tweetDB[followee]

        #heapq.heapify(totaltweets)
        
        ans = []
        while totaltweets and len(ans) < 10:
            ans.append(heapq.heappop(totaltweets)[1])
        ans.reverse()
            
        return ans
        
    def follow(self, followerId: int, followeeId: int) -> None:

        # register followeeId in followerId

        self.followDB[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        # deregister followeeId in followerId

        self.followDB[followerId].discard(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# key points
# user id <- follower (another user id)
# tweet id <- user id
# return most recent 10

# strategy

# 1. tweet DB : userid : (-time, tweetid)
# 2. follower DB : follower -< followee

# 3. store new tweet on leftmost, pop when it exceeds 10
#   tweet DB [ insert new -> [-5,5],[-4,3],[-3,101],[-2,13],[-1,10] <-- pop ]
#   follow DB [followerID] = [ followeeID1, followeeID2, followeeID3, ...]
# 4. newsfeed
#    collect all tweet from userid and followeeid
#    heapify
#    copy 10 most recent tweets to output
