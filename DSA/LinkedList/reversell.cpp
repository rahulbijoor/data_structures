#include<iostream>

using namespace std;

class LinkedList {
private:
    class Node {
    public:
        int data;
        Node* next;

        Node() {
            next = nullptr;
        }

        Node(int d) {
            data = d;
            next = nullptr;
        }

        Node(int d, Node* n) {
            data = d;
            next = n;
        }
    };

    Node* head;

public:
    LinkedList() {
        head = nullptr;
    }

    void insert(int value) {
        

        Node* newHead = new Node(value, head);
        head = newHead;
    }
    void insertAtTail(int value){
        Node* curr=head;
        if(head==nullptr){
            head=new Node(value);
            return;
        }
        Node* newtail=new Node(value);
        while(curr->next!=nullptr){
            curr=curr->next;
        }
        curr->next=newtail;
    }
    void reverse(){
        if(head==nullptr || head->next==nullptr){
            return;
        }
        Node* prev=nullptr;
        Node* curr=head;
        Node* after=nullptr;
        while(curr!=nullptr){
            after=curr->next;
            curr->next=prev;
            prev=curr;
            curr=after;
        }
        head=prev;
    }
    void print() {
        Node* curr = head;
        while (curr != nullptr) {
            cout << curr->data << " ";
            curr = curr->next;
        }
        cout << endl;
    }
};

int main() {
    LinkedList* list = new LinkedList(); 
    list->insertAtTail(10);
    list->insertAtTail(20);
    list->insertAtTail(30);
    list->print();
    list->reverse();
    list->print();

    delete list; 
    return 0;
}
