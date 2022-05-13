class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = [None] * (2 ** 5)

        for num in nums:
            depth = num // 100 - 1
            position = num // 10 % 10 - 1
            tree[2 ** depth - 1 + position] = num % 10

        ret = 0

        def dfs(pos: int, curr_sum: int) -> None:
            nonlocal ret
            if tree[pos] is None:
                return

            left = pos * 2 + 1
            right = pos * 2 + 2
            curr_sum += tree[pos]

            if tree[left] is None and tree[right] is None:
                ret += curr_sum
                return

            dfs(left, curr_sum)
            dfs(right, curr_sum)

        dfs(0, 0)
        return ret
