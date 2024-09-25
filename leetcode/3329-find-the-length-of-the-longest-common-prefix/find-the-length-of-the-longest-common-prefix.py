class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        for a in arr1:
            self.insert(a)
        maxLength = 0
        
        for a in arr2:
            curr = self.root
            count = 0
            for ch in a:
                if ch in curr.children:
                    curr = curr.children[ch]
                    count += 1
                else:
                    break
                maxLength = max(maxLength, count)
        return maxLength


        