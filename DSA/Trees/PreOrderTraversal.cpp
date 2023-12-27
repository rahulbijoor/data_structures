#include<iostream>
using namespace std;
#include<queue>
#include<stack>
class Tree{
    class Node{
        public:
            int data;
            Node* left;
            Node* right;
            Node(int data){
                this->data=data;
                this->left=nullptr;
                this->right=nullptr;
            }

    };
    Node* root;
    public:
    Tree(){
        root=nullptr;
    }
    void insert(int item){
        if(root==nullptr){
            root=new Node(item);
            return;
        }
        queue<Node*> queue;
        queue.push(root);
        Node* newNode=new Node(item);
        while(!queue.empty()){
            Node* current=queue.front();
            queue.pop();
            if(current->left!=nullptr){
                queue.push(current->left);
            }
            else{
                current->left=newNode;
                return;
            }
            if(current->right!=nullptr){
                queue.push(current->right);
            }
            else{
                current->right=newNode;
                return;
            }
        }

    }
    void PreOrder(){   //PreOrder traversal using while loop
        if(root==nullptr){
            return;
        }
        stack<Node*> stack;
        stack.push(root);
        vector<int> nodes;
        while(!stack.empty()){
            Node* current=stack.top();
            stack.pop();
            cout<<current->data<<", ";
            if(current->right!=nullptr){
                stack.push(current->right);
            }
            if(current->left!=nullptr){
                stack.push(current->left);
            }
            
            
            
        }
        cout<<endl;
    }
    void __PreOrderRecursive(Node* node){
        if(node==nullptr){
            return;
        }

        cout<<node->data<<", ";
        __PreOrderRecursive(node->left);
        __PreOrderRecursive(node->right);

    }
    void PreOrderRecursive(){ //PreOrder using Recursion
        if(root==nullptr){
            return;
        }
        __PreOrderRecursive(root);
        cout<<endl;
    }
};
int main(){
    Tree t;
    t.insert(10);
    t.insert(20);
    t.insert(30);
    t.insert(50);
    t.insert(40);
    t.PreOrderRecursive();
    return 0;
}
