# class Queue:
#     def __init__(self,size):
#         self.size = size
#         self.front = -1
#         self.rear = -1
#         self.queue = [0]*size
#     def enque(self,data):
#         if self.front == -1:
#             self.front=0
#             self.rear=0
#             self.queue[self.rear]=data
#             return
#         if self.rear == self.size-1:
#             print("is full")
#             return
#         self.rear+=1
#         self.queue[self.rear]=data
#
#     def deque(self):
#         if self.front==-1 or self.front>self.rear:
#             print("isempty")
#             return
#         self.front+=1
#
#     def Front(self):
#         if self.front==-1 or self.front>self.rear:
#             print("isempty")
#             return
#         print(f"front : {self.queue[self.front]}")
#     def display(self):
#         if self.front==-1 or self.front>self.rear:
#             print("isempty")
#             return
#         for i in range(self.front , self.rear+1):
#             print(self.queue[i],end=" ")
#
# obj = Queue(15)
# a = [9,3,4,12,0,34,2,22]
# for i in a:
#     obj.enque(i)
# obj.display()
#
#



class Queue:
    def __init__(self,size):
        self.queue = []
    def enque(self,data):
        self.queue.append(data)

    def deque(self):
        if len(self.queue)==0:
            print("isempty")
            return
        self.queue.pop(0)

    def Front(self):
        if len(self.queue) == 0:
            print("isempty")
            return
        print(f"front : {self.queue[0]}")
    def display(self):
        if len(self.queue) == 0:
            print("isempty")
            return
        for i in self.queue:
            print(i,end=" ")

obj = Queue(15)
a = [9,3,4,12,0,34,2,22]
for i in a:
    obj.enque(i)
obj.display()