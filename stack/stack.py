"""
Stack is a data structure which follows the last in, first out (LIFO) principle. The insertion and removal of elements can only be done from
one end. In python, we can use dynamic arrays to simulate a stack. We can use append() to push the element on the top of the stack and pop() to 
remove the elements from the top of the stack. Stack data structure supports following operations -
1. push(n) - push the element on the top of the stack
2. pop() - remove the top most element of the stack - assuming stack is not null
3. peek() - returns the top most element of the stack without removing it
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    # push the element on the top of the stack
    # [] -> push(2) -> [2 <- top] -> push(3) -> [2, 3 <- top]
    # O(1) time
    def push(self, n):
        self.stack.append(n)

    # remove the top most element of the stack - assuming stack is not null
    # we could also null check first and then if the stack is not empty then remove the element
    # O(1) time
    def pop(self):
        # check if the stack is not null
        if self.stack:
            self.stack.pop()

    # returns the top most element of the stack without removing it
    # O(1) time
    def peek(self):
        # check if the stack is not null
        if self.stack:
            return self.stack[len(self.stack) - 1]
        return None
    
    def display(self):
        print(self.stack)
    
s = Stack()
# push the few elements in the stack
s.push(1)
s.push(2)
s.push(3)
s.display() # [1, 2, 3]
s.pop()
s.display() # [1, 2]
s.pop()
s.display() # [1]
s.pop()
print(s.peek()) # 1
