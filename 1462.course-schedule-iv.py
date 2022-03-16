#
# @lc app=leetcode id=1462 lang=python3
#
# [1462] Course Schedule IV
#

# @lc code=start


from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dists = [[False] * numCourses for _ in range(numCourses)]

        for src, dest in prerequisites:
            dists[src][dest] = True

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dists[i][j] |= dists[i][k] and dists[k][j]

        return [dists[src][dest] for src, dest in queries]
        

    # Khan's algorithm
    #def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    #    graph = defaultdict(list)
    #    in_degree = [0] * numCourses
    #    depends = defaultdict(set)

    #    for src, dest in prerequisites:
    #        graph[src].append(dest)
    #        in_degree[dest] += 1
    #        depends[dest].add(src)

    #    queue = deque(c for c, i in enumerate(in_degree) if i == 0)
    #    
    #    while queue:
    #        curr = queue.popleft()
    #        for n in graph[curr]:
    #            depends[n] |= depends[curr]
    #            in_degree[n] -= 1
    #            if in_degree[n] == 0:
    #                queue.append(n)
    #            
    #    return [src in depends[dest] for src, dest in queries]
            

# @lc code=end

