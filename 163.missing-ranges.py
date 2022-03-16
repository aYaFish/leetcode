#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#

# @lc code=start
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        
        def toString(left: int, right: int) -> str:
            if left == right:
                return f"{left}"
            return f"{left}->{right}"

        lower -= 1
        nums.append(upper+1)

        for i in range(0, len(nums)):
            if nums[i] == lower + 1:
                lower = nums[i]
                continue
            ans.append(toString(lower+1, nums[i]-1))
            lower = nums[i]

        return ans



# @lc code=end

