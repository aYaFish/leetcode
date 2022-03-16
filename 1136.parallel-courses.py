#
# @lc app=leetcode id=1136 lang=python3
#
# [1136] Parallel Courses
#

# @lc code=start
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
        
        queue = deque(course for course in range(1, n+1) if in_degree[course] == 0)
        ans, count = 0, 0
        while queue:
            for _ in range(len(queue)):
                currCourse = queue.popleft()
                count += 1
                for course in graph[currCourse]:
                    in_degree[course] -= 1
                    if in_degree[course] == 0:
                        queue.append(course)
            ans += 1
        
        return ans if count == n else -1


# @lc code=end

