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
    void __rangeSum(TreeNode* n,int low,int high,int &sum){
        if(n==nullptr){
            return;
        }
        __rangeSum(n->left,low,high,sum);
        if(n->val>=low && n->val<=high){
            sum+=n->val;
        }
        __rangeSum(n->right,low,high,sum);
    }
    int rangeSumBST(TreeNode* root, int low, int high) {
        int sum=0;
        __rangeSum(root,low,high,sum);
        return sum;
    }
};