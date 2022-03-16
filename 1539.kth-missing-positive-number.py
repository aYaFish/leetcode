#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected = 1
        for num in arr:
            if num == expected:
                expected += 1
                continue
            if k <= num - expected:
                return expected + k - 1
            k -= num - expected
            expected = num + 1
        return expected + k - 1

        
# @lc code=end

