#
# @lc app=leetcode id=720 lang=python3
#
# [720] Longest Word in Dictionary
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end = False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = TrieNode()
        for word in words:
            curr = trie
            for letter in word:
                curr = curr.children[letter]
            curr.end = True

        ans = ""

        def dfs(path: str, node: TrieNode) -> None:
            nonlocal ans
            if len(path) > len(ans) or (len(path) == len(ans) and path < ans):
                ans = path

            for l, n in node.children.items():
                if n.end:
                    dfs(path + l, n)

        dfs("", trie)
        return ans


# @lc code=end
