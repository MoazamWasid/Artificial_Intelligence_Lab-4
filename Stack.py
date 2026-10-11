class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

#    def sort(self):
#        self.stack.sort()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


s = Stack()

size = int(input("Enter the size of the stack: "))  
print("Enter the elements:")

for i in range(size):
    s.push(int(input()))

s.display()


print("Popped:", s.pop())
print("Peek:", s.peek())

s.display()