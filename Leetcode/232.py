# https://leetcode.com/problems/implement-queue-using-stacks/
# Solution 1
# Python

class MyQueue :
    # Initialize your data structure
    def __init__(self) :
        self.stack1=[]
        self.stack2=[]
        self.front=0
    
    # Push element x to the back of queue
    def push(self, x: int) -> None :
        while self.stack1 : # Until there are no elements left in stack1,
            self.stack2.append(self.stack1.pop()) # pop the element in stack1 and add it to stack2 
        self.front=x
        self.stack1.append(x) # add 'x' to stack1 (the element in the back of the queue must be the "bottom" element of the stack)

        while self.stack2 : # Until there are no elements left in stack2,
            self.stack1.append(self.stack2.pop()) # pop the element in stack2 and add it to stack1 

    # Removes the element from in front of queue and returns that element
    def pop(self) -> int :
        return self.stack1.pop() # pop the element in stack1 (the element in front of the queue must be the "top" element of the stack)
    
    # Get the front element
    def peek(self) -> int :
        return self.stack1[-1] # return the element in the "top" of the stack (do not remove it from the stack)
    
    # Returns whether the queue is empty
    def empty(self) -> bool :
        return not self.stack1 # if stack1 is not empty, return false
    
        
