/*
 * @lc app=leetcode id=703 lang=cpp
 *
 * [703] Kth Largest Element in a Stream
 */

// @lc code=start
class KthLargest {
public:
    KthLargest(int k, vector<int>& nums): m_k(k) {
        for(int i : nums) {
            add(i);
        }
    }
    
    int add(int val) {
        m_pq.push(val);
        if(m_pq.size() > m_k) {
            m_pq.pop();
        }
        
        return m_pq.top();
    }
private:
    priority_queue<int, vector<int>, greater<int>> m_pq;
    int m_k;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
// @lc code=end

