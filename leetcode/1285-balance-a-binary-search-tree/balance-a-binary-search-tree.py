# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        sorted_values = inorder_traversal(root)
        
        # Step 2: Construct a balanced BST from sorted values
        def construct_balanced_bst(values):
            if not values:
                return None
            mid = len(values) // 2
            node = TreeNode(values[mid])
            node.left = construct_balanced_bst(values[:mid])
            node.right = construct_balanced_bst(values[mid+1:])
            return node
        
        return construct_balanced_bst(sorted_values)
