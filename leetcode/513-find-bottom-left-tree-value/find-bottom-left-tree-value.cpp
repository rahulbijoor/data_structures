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
    int findBottomLeftValue(TreeNode* root) {
        if(root==nullptr){
            return 0;
        }
        return findLeftMostNode(root);
    }
    int findLeftMostNode(TreeNode* root) {
    if (root == nullptr)
        return 0;
    
    queue<TreeNode*> q;
    q.push(root);
    TreeNode* leftmost = nullptr;

    while (!q.empty()) {
        int levelSize = q.size();

        for (int i = 0; i < levelSize; ++i) {
            TreeNode* node = q.front();
            q.pop();
   
            if (i == 0) {
                leftmost = node;
            }

            if (node->left)
                q.push(node->left);
            if (node->right)
                q.push(node->right);
        }
    }
    return leftmost->val;
}
};