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
    void inorder(TreeNode *root,int &ans,TreeNode *&prev){
        if(root==nullptr){
            return;
        }
        inorder(root -> left, ans, prev);
        if(prev){
            ans=min(ans,abs(prev->val-root->val));
        }
        prev=root;
        inorder(root->right,ans,prev);
    }
    int getMinimumDifference(TreeNode* root) {
        if(root==nullptr){
            return INT_MAX;
        }
        int ans=INT_MAX;
        TreeNode *prev= nullptr;
        inorder(root, ans, prev);
        return ans;
    }
};