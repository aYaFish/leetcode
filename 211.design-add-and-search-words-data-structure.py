#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.links = defaultdict(TrieNode)
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for letter in word:
            curr = curr.links[letter]
        curr.end = True

    # def search(self, word: str) -> bool:
    #     queue = deque([(self.root, 0)])
    #     while queue:
    #         curr, level = queue.popleft()
    #         if level == len(word):
    #             if curr.end:
    #                 return True
    #             continue
    #         if word[level] == ".":
    #             for node in curr.links.values():
    #                 queue.append((node, level+1))
    #         elif word[level] in curr.links:
    #             queue.append((curr.links[word[level]], level+1))

    #     return False

    def search(self, word: str) -> bool:
        def do_search(word: str, node: TrieNode) -> bool:
            for i, c in enumerate(word):
                if c in node.links:
                    node = node.links[c]
                else:
                    if c == ".":
                        for n in node.links.values():
                            if do_search(word[i+1:], n):
                                return True
                    return False
            return node.end
        return do_search(word, self.root)



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

