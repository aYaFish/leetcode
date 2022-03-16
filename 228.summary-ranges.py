#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    # def summaryRanges(self, nums: List[int]) -> List[str]:
    #     ans = []
    #     left, right = 0, 0
    #     while right < len(nums):
    #         if right + 1 < len(nums) and nums[right]+1 == nums[right+1]:
    #             right += 1
    #             continue

    #         if left == right:
    #             ans.append(f"{nums[right]}")
    #         else:
    #             ans.append(f"{nums[left]}->{nums[right]}")

    #         right += 1
    #         left = right
    #     return ans
            
    def summaryRanges(self, nums: List[int]) -> List[str]:
        window = []
        left = 0

        for i in range(0, len(nums)):
            # always look forward, otherwise extra steps need to be taken
            # after loop ends to close the last window
            if i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                continue
            right = i
            if nums[left] == nums[right]:
                window.append(f"{nums[right]}")
            else:
                window.append(f"{nums[left]}->{nums[right]}")
            left = i+1

        return window
    
        

# @lc code=end

