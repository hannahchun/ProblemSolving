// https://leetcode.com/problems/linked-list-cycle/
// Solution 1
// C++

#include <iostream>

using namespace std;

// Definition for singly-linked list.
struct ListNode {
    int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL) {
            return false;
        }
        ListNode *slow = head;
        ListNode *fast = head->next;
        while (slow != fast) {
            if (fast == NULL || fast->next == NULL) {
                return false;
            }
            slow = slow->next;
            fast = fast->next->next;
        }
        return true;
    }
};

int main() {
    // Create a sample linked list with a cycle
    ListNode *head = new ListNode(3);
    head->next = new ListNode(2);
    head->next->next = new ListNode(0);
    head->next->next->next = new ListNode(-4);
    head->next->next->next->next = head->next;

    Solution sol1;
    bool isCycle = sol1.hasCycle(head);

    if (isCycle) {
        cout << "The linked list has a cycle." << endl;
    } 
    else {
        cout << "The linked list does not have a cycle." << endl;
    }
    return 0;
}
