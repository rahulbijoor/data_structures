#include<iostream>
using namespace std;
#include<queue>
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
    void BFS(){
        queue<Node*> queue;
        queue.push(root);
       
        while(!queue.empty()){
            Node* current=queue.front();
            queue.pop();
            cout<<current->data<<", ";
            if(current->left!=nullptr){
                queue.push(current->left);
            }
            
            if(current->right!=nullptr){
                queue.push(current->right);
            }
            
        }
        cout<<endl;
    }
    void __BFSRecursive(queue<Node*>& queue){
        if(queue.empty()){
            return;
        }
        Node* current=queue.front();
        queue.pop();
        cout<<current->data<<", ";
        if(current->left!=nullptr){
            queue.push(current->left);
        }
        if(current->right!=nullptr){
            queue.push(current->right);
        }
        __BFSRecursive(queue);

    }
    void BFSRecursive(){
        if(root==nullptr){
            return;
        }
        queue<Node*> queue;
        queue.push(root);
        __BFSRecursive(queue);
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
    t.BFSRecursive();
    return 0;
}
