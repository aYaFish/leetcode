#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        M, N = len(nums1), len(nums2)
        if M > N:
            return self.findMedianSortedArrays(nums2, nums1)

        left, right = 0, M * 2
        while left <= right:
            pos_m = (left + right) // 2
            pos_n = M + N - pos_m

            left_m = nums1[(pos_m - 1) // 2] if pos_m > 0 else float("-inf")
            left_n = nums2[(pos_n - 1) // 2] if pos_n > 0 else float("-inf")
            right_m = nums1[pos_m // 2] if pos_m != M * 2 else float("inf")
            right_n = nums2[pos_n // 2] if pos_n != N * 2 else float("inf")

            if left_m > right_n:
                right = pos_m - 1
            elif left_n > right_m:
                left = pos_m + 1
            else:
                return (max(left_m, left_n) + min(right_m, right_n)) / 2

        return float("-inf")


# @lc code=end
