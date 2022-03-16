#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#

# @lc code=start
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = self.buildTrie(dictionary)

        word_list = sentence.split(" ")
        for i, word in enumerate(word_list):
            word_list[i] = word[:self.searchTrie(root, word)]
        return " ".join(word_list)
            
    def searchTrie(self, root: TrieNode, word: str) -> int:
        length = 0
        for letter in word:
            if letter not in root.children or root.end:
                break
            root = root.children[letter]
            length += 1
        return length if root.end else len(word)

    def buildTrie(self, dictionary: List[str]) -> TrieNode:
        root = TrieNode()
        for word in dictionary:
            curr = root
            for letter in word:
                curr = curr.children[letter]
            curr.end = True
        return root
        
# @lc code=end

