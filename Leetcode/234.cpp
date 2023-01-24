// https://leetcode.com/problems/palindrome-linked-list/
// Solution 1
// C++

#include <iostream>
#include <stack>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public :
        bool isPalindrome(ListNode* head) {
            // stack
            stack <int> s;
            ListNode* node = head;    

            // push a node into the stack 
            while (node != NULL) {
                s.push(node->val); 
                node = node->next; // move on to the next node
            }

            // traverse
            node = head;
            while(node != NULL) {
                int top = s.top(); // get the element in the top of the stack
                s.pop();

                // compare the popped element with the current node's data
                if(top != node->val)
                    return false;
                node = node->next; // move on to the next node
            }
            return true;
        }
};

int main() {
    Solution s1;

    ListNode *head = new ListNode(1);
    head->next = new ListNode(4);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(2);
    head->next->next->next->next = new ListNode(1);

    if(s1.isPalindrome(head)) {
        cout << "Linked List is a palindrome."<<"\n";
    }
    else {
        cout << "Linked List is not a palindrome."<<"\n";
    }
    return 0;
}