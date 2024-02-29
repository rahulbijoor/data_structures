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
    bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> qt;
        if(root==nullptr){
            return true;
        }
        qt.push(root);
        vector<vector<TreeNode*>> levels;
        while(!qt.empty()){
            int levelSize=qt.size();
            vector<TreeNode*> level;
            for(int i=0;i<levelSize;i++){
                TreeNode* top=qt.front();
                qt.pop();
                if(top!=nullptr){
                level.push_back(top);
                }
                if(top->left){
                    qt.push(top->left);
                }
                if(top->right){
                    qt.push(top->right);
                }
            }
            levels.push_back(level);

        }
        for(int i=0;i<levels.size();i++){
            for(int j=0;j<levels[i].size();j++){
                cout<<levels[i][j]->val<<", ";
            }
            cout<<endl;
        }
        for(int i=0;i<levels.size();i++){
            if(i%2==0){
                int l=levels[i].size();
                for(int j=0;j<levels[i].size()-1;j++){
                    if(levels[i][j]->val%2==0){
                        return false;
                    }
                    if(levels[i][j]->val>=levels[i][j+1]->val){
                        return false;
                    }
                }
                if(levels[i][l-1]->val%2==0){
                    return false;
                }
            }
            else{
                int l=levels[i].size();
                for(int j=0;j<levels[i].size()-1;j++){
                     if(levels[i][j]->val%2==1){
                        return false;
                    }
                     if(levels[i][j]->val<=levels[i][j+1]->val){
                        return false;
                    }
                }
                if(levels[i][l-1]->val%2==1){
                    return false;
                }
            }
        }
        return true;

    }
};