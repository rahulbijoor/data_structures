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
    list->insert(10);
    list->insert(20);
    list->insert(30);
    list->print();

    delete list; 
    return 0;
}
