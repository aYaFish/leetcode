/*
 * @lc app=leetcode id=277 lang=cpp
 *
 * [277] Find the Celebrity
 */

// @lc code=start
/* The knows API is defined for you.
      bool knows(int a, int b); */

class Solution {
public:
    int findCelebrity(int n) {
        // logical deduction
        // if a knows b, then a can't be a celeb, b/c celeb doesn't know anyone
        // if a doesn't know b, then b can't be a celeb, b/c everyone knows celeb
        int candidate = 0;
        for(int i=1; i<n; ++i) {
            if(knows(candidate, i)) {
                candidate = i;
            }
        }

        for(int i=0; i<n; ++i) {
            if(candidate == i) continue;
            if(!knows(i, candidate) || knows(candidate, i)) {
                return -1;
            }
        }
        return candidate;
    }
};
// @lc code=end

