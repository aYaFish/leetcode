#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#

# @lc code=start
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        letters = Counter(s)
        odd_count, half_length, odd_letter = 0, 0, ""
        for l in letters:
            if letters[l] % 2 != 0:
                odd_count += 1
                odd_letter = l
            letters[l] //= 2
            half_length += letters[l]
        
        if odd_count > 1:
            return []
        
        path, ans = [], []
        def dfs():
            if len(path) == half_length:
                a = "".join(path)
                ans.append(a + odd_letter + a[::-1])
                return
            
            for l in letters:
                if letters[l] == 0:
                    continue
                path.append(l)
                letters[l] -= 1
                dfs()
                path.pop()
                letters[l] += 1
        
        dfs()
        return ans

# @lc code=end

