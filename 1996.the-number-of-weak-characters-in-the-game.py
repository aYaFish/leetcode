#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#

# @lc code=start
from collections import deque

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_attack = max(properties, key=lambda element: element[0])[0]
        max_defenses = [0 for _ in range(max_attack + 2)]
        
        for attack, defense in properties:
            max_defenses[attack] = max(max_defenses[attack], defense)
        
        for index in range(max_attack, 0, -1):
            max_defenses[index] = max(max_defenses[index], max_defenses[index + 1])
        
        count = 0
        for attack, defense in properties:
            if defense < max_defenses[attack + 1]:
                count += 1

        return count

    # def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
    #     properties.sort(key=lambda ele: (ele[0], -ele[1]))
    #     max_defense, count = 0, 0
    #     for _, defense in properties[::-1]:
    #         if defense < max_defense:
    #             count += 1
    #         max_defense = max(defense, max_defense)
        
    #     return count
        
# @lc code=end

