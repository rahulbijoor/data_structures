/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        if(root==nullptr){
            return 0;
        }
        return diameter(root);
    }
    int height(TreeNode* n){
        if(n==nullptr){
            return 0;
        }
        return 1+ max(height(n->left),height(n->right));
    }
    int diameter(TreeNode* node){
        if(node==nullptr){
            return 0;
        }
        int leftHeight=height(node->left);
        int rightHeight=height(node->right);
        int leftdiameter=diameter(node->left);
        int rightdiameter=diameter(node->right);
        return max(leftHeight+rightHeight,max(leftdiameter,rightdiameter));
    }
};