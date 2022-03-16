/*
 * @lc app=leetcode id=489 lang=cpp
 *
 * [489] Robot Room Cleaner
 */

// @lc code=start
/**
 * // This is the robot's control interface.
 * // You should not implement it, or speculate about its implementation
 * class Robot {
 *   public:
 *     // Returns true if the cell in front is open and robot moves into the
 * cell.
 *     // Returns false if the cell in front is blocked and robot stays in the
 * current cell. bool move();
 *
 *     // Robot will stay in the same cell after calling turnLeft/turnRight.
 *     // Each turn will be 90 degrees.
 *     void turnLeft();
 *     void turnRight();
 *
 *     // Clean the current cell.
 *     void clean();
 * };
 */

class Solution {
 public:
  vector<pair<int, int>> directs = {
      {-1, 0}, {0, -1}, {1, 0}, {0, 1}};  // counter-clock wise
  void cleanRoom(Robot &robot) {
    unordered_set<string> visited;
    dfs(robot, 0, 0, 0, visited);
  }

  void dfs(Robot &robot, int x, int y, int facing,
           unordered_set<string> &visited) {
    visited.insert(genKey(x, y));
    robot.clean();

    facing %= 4;
    // robot turns back to original facing after loop ends
    for (int k = 0; k < 4; ++k) {
      int next_facing = facing + k;
      int i = x + directs[next_facing % 4].first;
      int j = y + directs[next_facing % 4].second;
      if (!visited.count(genKey(i, j)) and robot.move()) {
        dfs(robot, i, j, next_facing, visited);

        // turnaround, move and turnaround, so it goes back
        // to position and facing the same way before dfs call
        robot.turnLeft();
        robot.turnLeft();
        robot.move();
        robot.turnLeft();
        robot.turnLeft();
      }
      robot.turnLeft();
    }
  }

  string genKey(int x, int y) {
    stringstream ss;
    ss << x << ',' << y;
    return ss.str();
  }
};
// @lc code=end
