#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class MagicDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            curr = self.trie
            for letter in word:
                curr = curr.children[letter]
            curr.end = True

    def search(self, searchWord: str) -> bool:
        def do_search(node: TrieNode, searchWord: str, change: bool) -> bool:
            if not searchWord:
                return node.end and change
            if not change:
                return any(
                    do_search(n, searchWord[1:], searchWord[0] != k)
                    for k, n in node.children.items()
                )
            if searchWord[0] in node.children:
                return do_search(
                    node.children[searchWord[0]], searchWord[1:], change
                )
            return False

        return do_search(self.trie, searchWord, False)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# @lc code=end
