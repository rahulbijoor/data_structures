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
    int __maxAncestorDiff(TreeNode* node,int maxi,int mini){
        if(node==nullptr){
            return maxi-mini;
        }
        mini=min(mini,node->val);
        maxi=max(maxi,node->val);
        int leftDiff=__maxAncestorDiff(node->left,maxi,mini);
        int rightDiff=__maxAncestorDiff(node->right,maxi,mini);
        return max(leftDiff,rightDiff);
    }  
    int maxAncestorDiff(TreeNode* root) {
        if(root==nullptr){
            return 0;
        }
        return __maxAncestorDiff(root,root->val,root->val);
        
    }
};