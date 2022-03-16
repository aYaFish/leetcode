#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # no circle
        graph = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])

        state = [0 for _ in range(numCourses)]
        
        def dfs(node: int) -> bool:
            state[node] = 1
            for t in graph[node]:
                if state[t] == 1:
                    return False
                if state[t] == 0 and not dfs(t):
                    return False
            state[node] = 2
            return True
        
        for i in range(numCourses):
            if state[i] == 0 and not dfs(i):
                return False
        
        return True

                    


            


# @lc code=end

