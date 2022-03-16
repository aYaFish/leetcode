/*
 * @lc app=leetcode id=1570 lang=cpp
 *
 * [1570] Dot Product of Two Sparse Vectors
 */

// @lc code=start
class SparseVector {
public:
    
    SparseVector(vector<int> &nums) {
        for(int i=0; i<nums.size(); ++i) {
            if(nums[i]) {
                hash[i] = nums[i];
            }
        }
    }
    
    // Return the dotProduct of two sparse vectors
    int dotProduct(SparseVector& vec) {
        int ans = 0;
        for(auto& item : hash) {
            ans += item.second * vec.getValue(item.first);
        }

        return ans;
    }

    int getValue(int key) {
        if(hash.count(key)) {
            return hash[key];
        }
        return 0;
    }

private:
    unordered_map<int, int> hash;
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);
// @lc code=end

