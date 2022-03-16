#
# @lc app=leetcode id=1570 lang=python3
#
# [1570] Dot Product of Two Sparse Vectors
#

# @lc code=start
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, num in enumerate(nums):
            if num != 0:
                self.pairs.append([i, num])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        p, q = 0, 0
        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                ans += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1

        return ans

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# @lc code=end

