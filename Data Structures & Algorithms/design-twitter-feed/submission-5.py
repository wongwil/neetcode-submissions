class Twitter:

    def __init__(self):
        self.count = 0
        self.followees = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        k = 10
        res = []
        myheap = []

        self.followees[userId].add(userId) # add him/herself
        followees = self.followees[userId]

        for followee in followees:
            if followee in self.tweets: # if bro has some tweets
                index = len(self.tweets[followee]) - 1 # the index of the right most tweet, i.e. newest
                count, tweet = self.tweets[followee][index]
                heapq.heappush(myheap, [count, tweet, index, followee]) # so we can find the next newest tweet to append later (we need the index and which followee)

        while len(res) < k and myheap:
            count, newestTweet, index, followee = heapq.heappop(myheap)
            res.append(newestTweet)

            # k-merge: next element from that list goes into the heap
            if index > 0:
                nextIndex = index - 1
                count, nextTweet = self.tweets[followee][nextIndex]
                heapq.heappush(myheap, [count, nextTweet, nextIndex, followee])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)
