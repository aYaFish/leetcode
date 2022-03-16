#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#

# @lc code=start
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)

        def dfs() -> int:
            sum = 1
            for l in counter:
                if counter[l] == 0:
                    continue
                counter[l] -= 1
                sum += dfs()
                counter[l] += 1
            return sum
        
        return dfs() - 1 # Remove empty seq at the first run.


            
# @lc code=end

