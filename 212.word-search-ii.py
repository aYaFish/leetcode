#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])
        seen = [[False] * COLS for _ in range(ROWS)]
        trie = TrieNode()

        for word in words:
            curr = trie
            for letter in word:
                curr = curr.children[letter]
            curr.word = word

        def dfs(i: int, j: int, node: TrieNode) -> None:
            nonlocal seen, ans
            if node.word:
                ans.add(node.word)
            seen[i][j] = True
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if (
                    x < 0
                    or x == ROWS
                    or y < 0
                    or y == COLS
                    or seen[x][y]
                    or board[x][y] not in node.children
                ):
                    continue
                dfs(x, y, node.children[board[x][y]])
            seen[i][j] = False

        ans = set()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in trie.children:
                    dfs(i, j, trie.children[board[i][j]])

        return ans


# @lc code=end
