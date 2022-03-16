class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.N = len(words[0])
        path, result = [], []
        
        # self.buildTrie()
        self.buildPrefixHash()
        
        for word in words:
            path = [word]
            self.dfs(1, path, result)
        
        return result
        
    def dfs(self, pos: int, path: List[str], result: List[List[str]]) -> None:
        if pos == self.N:
            result.append(path[:])
            return
        
        prefix = ''.join([word[pos] for word in path])
        for word in self.getWordsWithPrefix(prefix):
            path.append(word)
            self.dfs(pos+1, path, result)
            path.pop()
    
    def buildPrefixHash(self) -> None:
        self.prefixHash = defaultdict(list)
        for word in self.words:
            for prefix in [word[:i] for i in range(1, len(word))]:
                self.prefixHash[prefix].append(word)
                
    def getWordsWithPrefix(self, prefix: str) -> List[str]:
        return self.prefixHash[prefix]
    
    # def buildTrie(self) -> None:
    #     self.trie = {}
    #     for index, word in enumerate(self.words):
    #         node = self.trie
    #         for c in word:
    #             if not c in node:
    #                 node[c] = {'#': []}
    #             node = node[c]
    #             node["#"].append(index)
    
    # def getWordsWithPrefix(self, prefix: str) -> List[str]:
    #     node = self.trie
    #     for c in prefix:
    #         if not c in node:
    #             return []
    #         node = node[c]
    #     return [self.words[index] for index in node['#']]
