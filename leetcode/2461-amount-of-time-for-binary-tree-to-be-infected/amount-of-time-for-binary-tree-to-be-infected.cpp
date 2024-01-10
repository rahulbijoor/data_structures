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
    void convertGraph(TreeNode* node,int parent,unordered_map<int,unordered_set<int>> &map){
        if(node==nullptr){
            return;
        }
        if(map.find(node->val)==map.end()){
            map[node->val]=unordered_set<int>();
        }
        unordered_set<int>& adjacentList = map[node->val];
        if(parent!=0){
            adjacentList.insert(parent);
        }
        if(node->left!=nullptr){
            adjacentList.insert(node->left->val);
        }
        if(node->right!=nullptr){
            adjacentList.insert(node->right->val);
        }
        convertGraph(node->left,node->val,map);
        convertGraph(node->right,node->val,map);


    }
    int amountOfTime(TreeNode* root, int start) {
        unordered_map<int,unordered_set<int>> map;
        convertGraph(root,0,map);
        queue<int> q;
        q.push(start);
        int minute=0;
        unordered_set<int> visited;
        visited.insert(start);
        while(!q.empty()){
            int levelSize=q.size();
            while(levelSize>0){
                int curr=q.front();
                q.pop();
                for(int num:map[curr]){
                    if(visited.find(num)==visited.end()){
                        visited.insert(num);
                        q.push(num);
                    }

                }
                levelSize--;
            }
            minute++;
        }
        return minute-1;

    }
};