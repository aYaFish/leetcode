#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # For set intersections, consider bitmask
        hashmap = defaultdict(int)
        for word in words:
            bitmask = 0
            for l in word:
                bitmask |= 1 << (ord(l) - ord('a'))
            hashmap[bitmask] = max(hashmap[bitmask], len(word))

        
        ans = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    ans = max(ans, hashmap[x]*hashmap[y])
        
        return ans


# @lc code=end

