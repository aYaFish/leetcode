#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        state = [0 for _ in range(numCourses)]
        ans = []
        
        def dfs(node: int) -> bool:
            state[node] = 1
            for t in graph[node]:
                if state[t] == 1:
                    return False
                if state[t] == 0 and not dfs(t):
                    return False
            state[node] = 2
            ans.append(node)
            return True
        
        for i in range(numCourses):
            if state[i] == 0 and not dfs(i):
                return []
        
        return ans
# @lc code=end

