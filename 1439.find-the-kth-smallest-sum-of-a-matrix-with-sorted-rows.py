#
# @lc app=leetcode id=1439 lang=python3
#
# [1439] Find the Kth Smallest Sum of a Matrix With Sorted Rows
#

# @lc code=start
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        if len(mat) == 1:
            return mat[0][k-1]

        ans = self.kSmallestPairs(mat[0], mat[1], k)
        for i in range(2, len(mat)):
            ans = self.kSmallestPairs(ans, mat[i], k)

        return ans[k-1]
    
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # convert this to 378, matrix is made by sum of nums1 and nums2
        # e.g matrix[i][j] = nums1[i] + nums2[j]
        # this way each row is sorted and each col is sorted
        # we just need to maintain a min heap with size k
        minHeap = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while minHeap and k:
            val, i, j = heapq.heappop(minHeap)
            ans.append(val)

            if j+1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[j+1], i, j+1))
            
            k -= 1

        return ans

        
        


        
# @lc code=end

