#
# @lc app=leetcode id=642 lang=python3
#
# [642] Design Search Autocomplete System
#

# @lc code=start
from collections import defaultdict


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = {}
        self.sentences = defaultdict(int)

        self.prefix = ""
        self.position = self.trie

        for s, t in zip(sentences, times):
            self.store(s, t)

    def store(self, sentence, time):
        curr = self.trie
        self.sentences[sentence] -= time
        for l in sentence:
            if l not in curr:
                curr[l] = {"#": set()}
            curr = curr[l]
            curr["#"].add(sentence)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.store(self.prefix, 1)
            self.prefix = ""
            self.position = self.trie
            return []
        else:
            self.prefix += c
            if c not in self.position:
                self.position[c] = {"#": set()}
            self.position = self.position[c]
            return [
                s
                for _, s in heapq.nsmallest(
                    3, [(self.sentences[x], x) for x in self.position["#"]]
                )
            ]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# @lc code=end
