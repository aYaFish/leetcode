#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
class Solution:
    # def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #     ans, window = [], []
    #     for i in range(len(nums)):
    #         if i >= k:
    #             window.pop(bisect.bisect(window, nums[i-k])-1)
    #         bisect.insort(window, nums[i])

    #         if i >= k-1:
    #             ans.append(float(window[k//2])
    #                 if k&1
    #                 else (window[k//2-1]+window[k//2]) / 2
    #             )
    #     return ans

    # def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    #     lo, hi = [], []
    #     for i in range(k):
    #         heapq.heappush(lo, -nums[i])
    #     for _ in range(k//2): # lo is same size as hi or 1 more
    #         heapq.heappush(hi, -heapq.heappop(lo))

    #     ans = [float(-lo[0]) if k&1 else (hi[0]-lo[0])/2]
    #     lazy_remove = defaultdict(int)
    #     
    #     for i in range(k, len(nums)):
    #         # always push to lo
    #         heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))
    #         out_num = nums[i-k]

    #         # if out_num is in low, heap is balanced
    #         # else push to hi from lo to balance
    #         if out_num > -lo[0]:
    #             heapq.heappush(hi, -heapq.heappop(lo))

    #         lazy_remove[out_num] += 1

    #         # start remove from always push side, lo in this case
    #         # if out_num == -lo[0]
    #         # we need to remove from lo to maintain balance
    #         while lazy_remove[-lo[0]]:
    #             lazy_remove[-lo[0]] -= 1
    #             heapq.heappop(lo)
    #         while hi and lazy_remove[hi[0]]:
    #             lazy_remove[hi[0]] -= 1
    #             heapq.heappop(hi)
    #         
    #         # heaps must be balanced before we calculate median
    #         ans.append(float(-lo[0]) if k&1 else (hi[0]-lo[0])/2)
    #     
    #     return ans

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from sortedcontainers import SortedList
        sl = SortedList(nums[:k])
        ans = [float(sl[k//2]) if k&1 else (sl[k//2-1]+sl[k//2])*0.5]

        for i in range(k, len(nums)):
            if nums[i] != nums[i-k]:
                sl.remove(nums[i-k])
                sl.add(nums[i])
            ans.append(float(sl[k//2]) if k&1 else (sl[k//2-1]+sl[k//2])*0.5)
        
        return ans

        
# @lc code=end

