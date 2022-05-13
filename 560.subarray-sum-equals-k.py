#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        prefix_sum, count = 0, 0

        for num in nums:
            prefix_sum += num
            count += hashmap[prefix_sum - k]
            # Update map after adjusting count
            # This way we exclude prefix_sum at current position
            hashmap[prefix_sum] += 1

        return count


# @lc code=end
