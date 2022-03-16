#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        letters = Counter(s)

        count = 0
        for l, c in letters.items():
            if c%2 != 0:
                count += 1
        
        return count < 2


# @lc code=end

