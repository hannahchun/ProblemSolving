# https://leetcode.com/problems/palindrome-linked-list/
# Solution 2
# Python

from collections import deque

class ListNode :
    def __init__(self, val = 0, next = None) :
        self.val = val
        self.next = next
    
class Solution :
    def isPalindrome(self, head : ListNode) -> bool :
        dq = deque()

        # insert a node to the right end of the deque
        while head != None :
            dq.append(head.val)
            head = head.next
        while len(dq) > 1 :
            right = dq.pop() # pop an element from the right end of the deque
            left = dq.popleft() # pop an element from the left end of the deque
            if right != left : # compare the values
                return False
        return True

if __name__ == '__main__' :

    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    if Solution.isPalindrome(Solution, head) :
        print('Linked List is a palindrome.')
    else :
        print('Linked List is not a palindrome.')