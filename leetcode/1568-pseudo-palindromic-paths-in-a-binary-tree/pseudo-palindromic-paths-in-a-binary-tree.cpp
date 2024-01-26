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
    void DFSTraversal(TreeNode* node,vector<int>& freq,int &paths){
        if(node==nullptr){
            return;
        }
        if((node->left==nullptr)&&(node->right==nullptr)){
            freq[node->val]++;
            int odd=0;
            for(int i=0;i<freq.size();i++){
                if(freq[i]%2==1){
                    odd++;
                }
            }
            if(odd<2){
                paths++;
            }
            freq[node->val]--;
            return;
        }
        freq[node->val]++;
        DFSTraversal(node->left,freq,paths);
        DFSTraversal(node->right,freq,paths);
        freq[node->val]--;
    }
    int pseudoPalindromicPaths (TreeNode* root) {
        vector<int> freq(10,0);
        int paths=0;
        DFSTraversal(root,freq,paths);
        return paths;
    }
};