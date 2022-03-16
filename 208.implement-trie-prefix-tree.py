#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start

from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            curr = curr.links[letter]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.links:
                return False
            curr = curr.links[letter]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.links:
                return False
            curr = curr.links[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

