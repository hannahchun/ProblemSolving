// https://leetcode.com/problems/reverse-linked-list/
// Solution 1
// C++

#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
    public :
        // 데이타구조 수업 19.LinkedList응용 PPT에서 공부한 방법
        ListNode * reverseList(ListNode* head) {
            if (head == NULL || head->next == NULL)
                return head;
            ListNode *newhead = NULL;
            ListNode *oldhead = head;
            ListNode *tmp = new ListNode;
            while (oldhead != NULL) {
                tmp = newhead;
                newhead = oldhead;
                oldhead = oldhead ->next;
                newhead->next = tmp;
            }
            return newhead;
        }

        void print(ListNode *head) {
            ListNode *t = head;
            while(t != NULL) {
                cout<<t->val<<" ";
                t=t->next;
            }
            cout<<"\n";
        }
};

int main() {
    Solution s1;
    
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    head->next->next->next = new ListNode(2);
    head->next->next->next->next = new ListNode(1);

    ListNode *head2 = s1.reverseList(head);
    s1.print(head2);
    return 0;
}