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
    void __leafNodes(TreeNode* node,vector<int> &leaf){
        if(node==nullptr){
            return;
        }
        __leafNodes(node->left,leaf);
        if(node->left==nullptr && node->right==nullptr){
            leaf.push_back(node->val);
        }
        __leafNodes(node->right,leaf);
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaf1;
        vector<int> leaf2;
        __leafNodes(root1,leaf1);
        __leafNodes(root2,leaf2);
        if(leaf1.size()!=leaf2.size()){
            return false;
        }
        for(int i=0;i<leaf1.size();i++){
            if(leaf1[i]!=leaf2[i]){
                return false;
            }
        }
        return true;
    }
};