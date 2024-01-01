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
    void Inorder(TreeNode* n,vector<int>& values){
        if(n==nullptr){
            return;
        }
        Inorder(n->left,values);
        values.push_back(n->val);
        Inorder(n->right,values);
    }
    int kthSmallest(TreeNode* root, int k) {
        vector<int> values;
        Inorder(root,values);
        return values[k-1];
    }
};