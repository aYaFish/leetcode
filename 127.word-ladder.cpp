/*
 * @lc app=leetcode id=127 lang=cpp
 *
 * [127] Word Ladder
 */

// @lc code=start
class Solution {
 public:
  int ladderLength(string beginWord, string endWord, vector<string> &wordList) {
    unordered_set<string> words(wordList.begin(), wordList.end());
    if (words.count(endWord) == 0) return 0;

    unordered_set<string> beginSet, endSet;
    beginSet.insert(beginWord);
    endSet.insert(endWord);
    int level = 1, N = beginWord.size();
    while (!beginSet.empty() and !endSet.empty()) {
      if (beginSet.size() > endSet.size()) {
        beginSet.swap(endSet);
      }

      unordered_set<string> temp;
      for (auto w : beginSet) {
        for (int i = 0; i < N; ++i) {
          char t = w[i];
          for (int k = 'a'; k <= 'z'; ++k) {
            w[i] = k;
            if (endSet.count(w)) {
              return level + 1;
            }
            if (words.count(w)) {
              temp.insert(w);
              words.erase(w);
            }
          }
          w[i] = t;
        }
      }
      ++level;
      beginSet.swap(temp);
    }
    return 0;
  }
};
// @lc code=end
