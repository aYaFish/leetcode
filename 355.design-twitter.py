#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
import itertools


class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(deque)
        self.timer = itertools.count(step=-1)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        feed = heapq.merge(*(self.tweets[u] for u in self.follows[userId]))
        return [t for _, t in itertools.islice(feed, 10)]
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end
