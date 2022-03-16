#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        currColor = image[sr][sc]
        if currColor == newColor: return image
        
        def dfs(row, col):
            if image[row][col] != currColor: return

            image[row][col] = newColor
            if row > 0: dfs(row-1, col)
            if row+1 < R: dfs(row+1, col)
            if col > 0: dfs(row, col-1)
            if col+1 < C: dfs(row, col+1)
        
        dfs(sr, sc)
        return image


        
# @lc code=end

