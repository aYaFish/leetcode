#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # convert this to 378, matrix is made by sum of nums1 and nums2
        # e.g matrix[i][j] = nums1[i] + nums2[j]
        # this way each row is sorted and each col is sorted
        # we just need to maintain a min heap with size k
        minHeap = []
        for i in range(min(len(nums1), k)):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while minHeap and k:
            _, i, j = heapq.heappop(minHeap)
            ans.append([nums1[i], nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(minHeap, (nums1[i] + nums2[j+1], i, j+1))
            
            k -= 1

        return ans

# @lc code=end

