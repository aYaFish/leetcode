#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#

# @lc code=start
from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # Fully covered board: All tiles on board are covered by a domino or a tromino.

        # Partially covered board: Same as a fully covered board, except leave the
        # tile in the upper-right corner (the top row of the rightmost column)
        # uncovered. Note, a board with only the lower-right corner uncovered is
        # also considered "partially covered." However, as we will discover soon,
        # we do not need to keep track of which corner is uncovered because of symmetry.

        # f(k): The number of ways to fully cover a board of width k.
        # p(k): The number of ways to partially cover a board of width k.
        @cache
        def part_tiling(n: int) -> int:
            if n == 2:
                return 1

            # Adding a horizontal domino to a partially covered board of width n-1
            # Adding a tromino to a fully covered board of width n-2
            return (part_tiling(n - 1) + full_tiling(n - 2)) % MOD

        @cache
        def full_tiling(n: int) -> int:
            if n < 3:
                return n
            return (
                full_tiling(n - 1) + full_tiling(n - 2) + 2 * part_tiling(n - 1)
            ) % MOD

        return full_tiling(n)


# @lc code=end
