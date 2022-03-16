#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#

# @lc code=start
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        for x, y in edges:
            union(x, y)
        return len({find(x) for x in parent})

# @lc code=end

