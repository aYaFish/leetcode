#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#

# @lc code=start
Trie = lambda: defaultdict(Trie)

class WordFilter:
    # def __init__(self, words: List[str]):
    #     self.hashmap = {}

    #     def addTrie(root, index, word, step):
    #         if self.hashmap.get(word, index) != index:
    #             self.hashmap[word] = index
    #             return
    #         self.hashmap[word] = index
    #         for letter in word[::step]:
    #             if letter not in root:
    #                 root[letter] = {"#": set()}
    #             root = root[letter]
    #             root["#"].add(word)

    #     self.prefix_trie = {}
    #     self.suffix_trie = {}
    #     for index, word in enumerate(words):
    #         addTrie(self.prefix_trie, index, word, 1)
    #         addTrie(self.suffix_trie, index, word, -1)

    # def f(self, prefix: str, suffix: str) -> int:
    #     def searchTrie(root, letters):
    #         for letter in letters:
    #             if letter not in root:
    #                 return set()
    #             root = root[letter]
    #         return root["#"]

    #     found = searchTrie(self.prefix_trie, prefix[:]) & searchTrie(
    #         self.suffix_trie, suffix[::-1]
    #     )
    #     ans = -1
    #     for word in found:
    #         ans = max(ans, self.hashmap[word])
    #     return ans

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for weight, word in enumerate(words):
            for i in range(len(word)+1):
                curr = self.trie
                wrap = word[i:] + "#" + word
                for l in wrap:
                    curr = curr[l]
                    curr['$'] = weight


    def f(self, prefix: str, suffix: str) -> int:
        curr = self.trie
        for l in suffix + "#" + prefix:
            if l not in curr:
                return -1
            curr = curr[l]
        return curr["$"]


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
# @lc code=end
