#
# @lc app=leetcode id=1514 lang=python3
#
# [1514] Path with Maximum Probability
#

# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probs, graph = [0.0] * n, defaultdict(list)
        for index, (a, b) in enumerate(edges):
            graph[a].append((b, index)) # node, index of succProb
            graph[b].append((a, index))
        probs[start] = 1.0
        heap = [(-probs[start], start)] # prob, node
        visited = set()
        while heap:
            prob, curr = heapq.heappop(heap)
            if curr == end:
                return -prob
            if curr in visited:
                continue
            visited.add(curr)

            for neighbor, index in graph[curr]:
                if neighbor in visited:
                    continue
                cand = -prob * succProb[index]
                if cand > probs[neighbor]:
                    probs[neighbor] = cand
                    heapq.heappush(heap, (-probs[neighbor], neighbor))
        return probs[end]

# @lc code=end

