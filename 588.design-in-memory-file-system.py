#
# @lc app=leetcode id=588 lang=python3
#
# [588] Design In-Memory File System
#

# @lc code=start
from enum import IntFlag

class CountMode(IntFlag):
    FILE = 1
    DIR = 2
    BOTH = 3

class FileSystem:

    # class TrieNode:
    #     def __init__(self):
    #         self.children = defaultdict(FileSystem.TrieNode)
    #         self.file = False
    #         self.content = ""

    # def __init__(self):
    #     self.root = FileSystem.TrieNode()
        
    # def traverse(self, paths: List[str]) -> TrieNode:
    #     curr = self.root
    #     for p in paths:
    #         if not p: # split could generate empty str at begin/end
    #             continue
    #         curr = curr.children[p]
    #     return curr

    # def ls(self, path: str) -> List[str]:
    #     paths = path.split("/")
    #     node = self.traverse(paths)
    #     if node.file:
    #         return [paths[-1]]
    #     return sorted([k for k in node.children.keys()])

    # def mkdir(self, path: str) -> None:
    #     self.traverse(path.split("/"))

    # def addContentToFile(self, filePath: str, content: str) -> None:
    #     node = self.traverse(filePath.split("/"))
    #     node.content += content
    #     node.file = True

    # def readContentFromFile(self, filePath: str) -> str:
    #     node = self.traverse(filePath.split("/"))
    #     return node.content

    # def move(self, currPath: str, newPath: str) -> None:
    #     # Test move up/down following the same path
    #     currPaths = currPath.split("/")
    #     oldParent = self.traverse(currPaths[:-1])
    #     node = oldParent.children.pop(currPaths[-1])
    #     newPaths = newPath.split("/")
    #     newParent = self.traverse(newPaths[:-1])
    #     newParent.children[newPaths[-1]] = node
    
    # def count(self, path: str, mode: CountMode) -> int:
    #     # Test when path is file and dir
    #     node = self.traverse(path.split("/"))
    #     ret = 0
    #     if CountMode.FILE in mode:
    #         ret += sum(1 for n in node.children.values() if n.file)
    #         ret += 1 if node.file else 0
    #     if CountMode.DIR in mode:
    #         ret += sum(1 for n in node.children.values() if not n.file)
    #     return ret

    class TrieNode:
        def __init__(self):
            self.dirs = defaultdict(FileSystem.TrieNode)
            self.files = defaultdict(str)

    def __init__(self):
        self.root = FileSystem.TrieNode()
        
    def traverse(self, paths: List[str]) -> TrieNode:
        curr = self.root
        for p in paths:
            # if not p: # split could generate empty str at begin/end
            #     continue
            curr = curr.dirs[p]
        return curr

    def ls(self, path: str) -> List[str]:
        ret = []
        parent = self.root
        if path != "/":
            paths = path.strip("/").split("/")
            parent = self.traverse(paths[:-1])
            if paths[-1] in parent.files:
                return [paths[-1]]
            parent = parent.dirs[paths[-1]]
        ret += [k for k in parent.dirs.keys()]
        ret += [k for k in parent.files.keys()]
        return sorted(ret)

    def mkdir(self, path: str) -> None:
        if path == "/":
            return 
        paths = path.strip("/").split("/")
        parent = self.traverse(paths[:-1])
        parent = parent.dirs[paths[-1]]

    def addContentToFile(self, filePath: str, content: str) -> None:
        assert filePath != "/"
        paths = filePath.strip("/").split("/")
        parent = self.traverse(paths[:-1])
        parent.files[paths[-1]] += content

    def readContentFromFile(self, filePath: str) -> str:
        assert filePath != "/"
        paths = filePath.strip("/").split("/")
        parent = self.traverse(paths[:-1])
        return parent.files[paths[-1]]



# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
# @lc code=end

