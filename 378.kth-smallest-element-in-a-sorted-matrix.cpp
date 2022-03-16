/*
 * @lc app=leetcode id=378 lang=cpp
 *
 * [378] Kth Smallest Element in a Sorted Matrix
 */

// @lc code=start
// class Solution {
// public:
//     using Point = pair<int, int>;
//     int kthSmallest(vector<vector<int>>& matrix, int k) {
//         int N = matrix.size();
//         auto cmp = [&matrix](Point& a, Point& b) {
//             return matrix[a.first][a.second] > matrix[b.first][b.second];
//         };
// 
//         priority_queue<Point, vector<Point>, decltype(cmp)> pq(cmp);
//         for(int j=0; j<N; ++j) {
//             pq.push({j, 0});
//         }
// 
//         while(k>1) {
//             auto curr = pq.top();
//             pq.pop();
// 
//             if(curr.second + 1 < N) {
//                 pq.push({curr.first, curr.second+1});
//             }
//             --k;
//         }
// 
//         auto ans = pq.top();
//         return matrix[ans.first][ans.second];
//     }
// 
// };
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int N = matrix.size();
        int left = matrix[0][0], right = matrix[N-1][N-1];

        while(left < right) {
            int mid = left + (right - left) / 2;
            int less = matrix[0][0], more = matrix[N-1][N-1];
            int count = countLessEqual(matrix, mid, less, more);
            if(count == k) {
                return less;
            }
            if(count < k) {
                left = more;
            }
            else {
                right = less;
            }
        }
        return left;
    }

    int countLessEqual(vector<vector<int>>& matrix, int mid, int& less, int& more) {
        int N = matrix.size(), row = N-1, col = 0, count = 0;
        while(row>=0 and col<N) {
            if(matrix[row][col] > mid) {
                more = min(more, matrix[row][col]);
                --row;
            }
            else {
                less = max(less, matrix[row][col]);
                count += row + 1;
                ++col;
            }
        }
        return count;
    }
};
// @lc code=end

