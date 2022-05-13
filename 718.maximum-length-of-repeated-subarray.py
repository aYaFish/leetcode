#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        ans = 0
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])

        return ans


# @lc code=end
