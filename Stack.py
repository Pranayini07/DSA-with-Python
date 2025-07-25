class Stack:
    def __init__(self,size):
        self.stack = []
    def push(self,data):
        self.stack.append(data)

    def display(self):
        if len(self.stack) == 0:
            print("empty")
            return
        for i in self.stack[::-1]:
            print(i,end=" ")
    def peek(self):
        if  len(self.stack) ==0:
            print("empty")
            return
        print(self.stack[-1])
    
    def pop(self):
        if  len(self.stack) ==0:
            print("empty")
            return
        self.stack.pop()
obj = Stack(3)
obj.push(9)
obj.display()
print()
obj.pop()
obj.pop()
obj.display()