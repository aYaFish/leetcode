#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        left, right = 0, N - 1
        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        def search(left: int, right: int, reverse: bool = False) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                val = mountain_arr.get(mid)

                temp = target
                if reverse:
                    val, temp = temp, val

                if val < temp:
                    left = mid + 1
                elif val > temp:
                    right = mid - 1
                else:
                    return mid

            return -1

        ret = search(0, left)
        if ret != -1:
            return ret
        return search(left, N - 1, True)
        
# @lc code=end

