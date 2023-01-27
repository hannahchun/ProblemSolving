// https://leetcode.com/problems/middle-of-the-linked-list/
// Solution 1
// C++

#include <iostream>

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
    public:
        ListNode* middleNode(ListNode* head) {
            int length = listLength(head);
            ListNode * temp[length];
            int count = 0 ;
            while(head != nullptr) {
                temp[count] = head;
                count += 1;
                head = head->next;
            }
            return temp[count / 2];
        }

        int listLength(ListNode* head) {
            int length = 0;
            while(head != nullptr) {
                length += 1;
                head = head->next;
            }
            return length;
        }

        void printNode(ListNode *head) {
            ListNode *t = head;
            while(t != NULL) {
                cout<<t->val<<" ";
                t = t->next;
            }
            cout<<"\n";
        }
};

int main() {
    Solution s1;

    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(4);
    head->next->next->next->next = new ListNode(5);

    s1.printNode(s1.middleNode(head));
       
    return 0;
}