/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
        //Since we are not given the head of the linked list we cannot perform traversal of the linked list.
        //Instead we could copy the value of the next node and the point the current node to the node write after. This way the node right after the current node will not be accessible.
        node->val=node->next->val;
        node->next=node->next->next;
    }
};