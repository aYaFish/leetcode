#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
import enum
from sortedcontainers import SortedList
class Solution:
    # def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
    #     sl = SortedList()
    #     for i, num in enumerate(nums):
    #         pos = sl.bisect_left(num)
    #         if pos == len(sl):
    #             if pos and abs(num - sl[-1]) <= t:
    #                 return True
    #         elif pos == 0:
    #             if abs(num - sl[0]) <= t:
    #                 return True
    #         else:
    #             if abs(num - sl[pos]) <= t or abs(num - sl[pos-1]) <= t:
    #                 return True
    #         sl.add(num)
    #         if len(sl) > k:
    #             sl.remove(nums[i-k])
    #     return False
            
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = dict()
        w = t + 1 # avoid t==0; cover same butcket <= t [0, t] total t+1 elements
        for i, num in enumerate(nums):
            key = num // w
            if key in buckets:
                return True
            elif (key - 1) in buckets and abs(num - buckets[key - 1]) < w:
                return True
            elif (key + 1) in buckets and abs(num - buckets[key + 1]) < w:
                return True
            buckets[key] = num
            if i >= k:
                buckets.pop(nums[i-k] // w)
        return False
        
# @lc code=end

