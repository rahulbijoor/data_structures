"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copyMap = {}
        def deepCopy(node):
            if not node:
                return None
            if node in copyMap:
                return copyMap[node]
            copy = Node(node.val)
            copyMap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(deepCopy(nei))
            return copy
        return deepCopy(node)