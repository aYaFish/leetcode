/*
 * @lc app=leetcode id=126 lang=cpp
 *
 * [126] Word Ladder II
 */

// @lc code=start
/* class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord,
vector<string>& wordList) { unordered_set<string> words(wordList.begin(),
wordList.end()); vector<vector<string>> ans; if(words.count(endWord) == 0)
return ans;

        int N = beginWord.size();
        queue<string> que;
        que.push(beginWord);
        words.erase(beginWord);

        unordered_map<string, unordered_set<string>> graph;
        bool isFound = false;
        while(!que.empty() and !isFound) {
            int size = que.size();
            unordered_set<string> visited;
            for(int i=0; i<size; ++i) {
                string curr = que.front();
                que.pop();

                string temp(curr);
                for(int j=0; j<N; ++j) {
                    char c = temp[j];
                    for(char k='a'; k<='z'; ++k) {
                        temp[j] = k;
                        if(temp == endWord) {
                            isFound = true;
                        }
                        if(words.count(temp)) {
                            que.push(temp);
                            visited.insert(temp);
                            graph[curr].insert(temp);
                        }
                    }
                    temp[j] = c;
                }
            }
            for(auto& v : visited) {
                words.erase(v);
            }
        }

        if(!isFound) return ans;

        vector<string> currPath{beginWord};
        dfs(graph, beginWord, endWord, currPath, ans);

        return ans;
    }

    void dfs(unordered_map<string, unordered_set<string>>& graph,
             string& src,
             string& dest,
             vector<string>& currPath,
             vector<vector<string>>& ans) {
        if(src == dest) {
            ans.push_back(currPath);
            return;
        }

        for(auto s : graph[src]) {
            currPath.push_back(s);
            dfs(graph, s, dest, currPath, ans);
            currPath.pop_back();
        }
    }
}; */
class Solution {
 public:
  vector<vector<string>> findLadders(string beginWord, string endWord,
                                     vector<string> &wordList) {
    unordered_set<string> words(wordList.begin(), wordList.end());
    vector<vector<string>> ans;

    if (!words.count(endWord)) return ans;
    int N = beginWord.size();
    unordered_set<string> beginSet, endSet;
    unordered_map<string, unordered_set<string>> graph;

    beginSet.insert(beginWord);
    words.erase(beginWord);

    endSet.insert(endWord);
    words.erase(endWord);

    int direction = 1;
    bool isFound = false;

    while (!beginSet.empty() and !endSet.empty() and !isFound) {
      if (beginSet.size() > endSet.size()) {
        beginSet.swap(endSet);
        direction ^= 1;
      }

      unordered_set<string> tempSet;
      for (auto w : beginSet) {
        string s = w;
        for (int i = 0; i < N; ++i) {
          char c = s[i];
          for (char k = 'a'; k <= 'z'; ++k) {
            s[i] = k;
            if (endSet.count(s)) {
              isFound = true;
              addEdge(graph, w, s, direction);
            }
            if (words.count(s)) {
              tempSet.insert(s);
              addEdge(graph, w, s, direction);
            }
          }
          s[i] = c;
        }
      }
      for (auto &w : tempSet) {
        words.erase(w);
      }
      beginSet.swap(tempSet);
    }

    if (!isFound) return ans;

    vector<string> currPath{beginWord};
    dfs(graph, beginWord, endWord, currPath, ans);

    return ans;
  }

  void addEdge(unordered_map<string, unordered_set<string>> &graph,
               string &first, string &second, int direction) {
    if (direction) {
      graph[first].insert(second);
    } else {
      graph[second].insert(first);
    }
  }

  void dfs(unordered_map<string, unordered_set<string>> &graph, string &src,
           string &dest, vector<string> &currPath,
           vector<vector<string>> &ans) {
    if (src == dest) {
      ans.push_back(currPath);
      return;
    }

    for (auto s : graph[src]) {
      currPath.push_back(s);
      dfs(graph, s, dest, currPath, ans);
      currPath.pop_back();
    }
  }
};
// @lc code=end
