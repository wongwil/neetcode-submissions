class Twitter:

    def __init__(self):
        self.time = 0
        self.followee = defaultdict(set) # key: user x, val: people user x follows
        self.tweets = defaultdict(list) # tweets user x has made but in format (time, tweetId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1 # decrease because we want a min heap based on that

    def getNewsFeed(self, userId: int) -> List[int]:
        # include own tweets
        self.followee[userId].add(userId)

        res = []
        k = 10
        # k-merge: add each sorted list to heap, then iteratively select the top to the res
        myheap = []
        followees = self.followee[userId]

        for followee in followees:
            tweets = self.tweets[followee]
            if tweets:
                index = len(tweets) - 1
                time, mostRecentTweet = tweets[index]
                heapq.heappush(myheap, [time, mostRecentTweet, followee, index])

        while len(res) < k and myheap:
            time, mostRecentTweet, followee, index = heapq.heappop(myheap)

            res.append(mostRecentTweet)
            
            if index > 0:
                index -= 1
                tweets = self.tweets[followee]
                time, mostRecentTweet = tweets[index]
                heapq.heappush(myheap, [time, mostRecentTweet, followee, index])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followee[followerId].discard(followeeId)
