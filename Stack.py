# Using a list as a stack
s = []
s.append(1)  # Append 1 to the stack
s.append(2)  # Append 2 to the stack
s.append(3)  # Append 3 to the stack

s.pop()  # Remove and return the last item (3)
print(s[-1])  # Print the last item in the stack (2)

# Using deque from collections as a stack
from collections import deque

stack = deque()  # Create a deque object

print(dir(stack))  # Print all attributes and methods of deque

stack.append(11)  # Append 11 to the stack
stack.append(33)  # Append 33 to the stack
stack.append(44)  # Append 44 to the stack

print(stack)  # Print the current state of the stack

class Stack:
    def __init__(self):
        self.container = deque()  # Initialize an empty deque

    def push(self, val):
        self.container.append(val)  # Append value to the stack

    def pop(self):
        return self.container.pop()  # Remove and return the last item

    def peek(self):
        return self.container[-1]  # Return the last item without removing it

    def is_empty(self):
        return len(self.container) == 0  # Check if the stack is empty

    def size(self):
        return len(self.container)  # Return the size of the stack

# Test the Stack class
k = Stack()
k.push(2)  # Push 2 to the stack
k.push(22)  # Push 22 to the stack
k.push(23)  # Push 23 to the stack
k.push(4)  # Push 4 to the stack
print(k.peek())  # Print the top item (4)
k.pop()  # Remove and return the top item (4)
print(k.is_empty())  # Check if the stack is empty (False)
print(k.size())  # Print the size of the stack (3)
