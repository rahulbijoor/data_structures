# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSequence(self,node: Optional[TreeNode],leaf_Seq: List[int]):
        if not node:
            return  
        if not node.left and not node.right:
            leaf_Seq.append(node.val)
            return
        
        self.leafSequence(node.left,leaf_Seq)
        
        self.leafSequence(node.right,leaf_Seq)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1=[]
        leaf2=[]
        self.leafSequence(root1,leaf1)
        self.leafSequence(root2,leaf2)

        return leaf1 == leaf2
