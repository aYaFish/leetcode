#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from email import iterators


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def neighbors(word: str) -> Iterable:
            for i in range(len(word)):
                for j in range(26):
                    yield word[:i] + chr(j + ord('a')) + word[i + 1:]
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        graph = defaultdict(set)
        found = False
        queue = deque([beginWord])
        wordSet.discard(beginWord)
        while queue:
            count = itertools.count(len(queue), -1)
            visited = set()
            while next(count):
                curr = queue.popleft()

                for word in neighbors(curr):
                    if word in wordSet:
                        if word == endWord:
                            found = True
                        visited.add(word)
                        graph[curr].add(word)
            if found:
                break
            wordSet ^= visited
            queue.extend(visited)

        if not found:
            return []
        ans = []        
        def dfs(path: List[str]) -> None:
            if path[-1] == endWord:
                ans.append(path)
                return
            for nextWord in graph[path[-1]]:
                dfs(path + [nextWord])

        dfs([beginWord])
        return ans
        
# @lc code=end

