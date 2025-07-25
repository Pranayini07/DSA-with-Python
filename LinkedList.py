class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None

    def b_insert(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def display(self):
        if self.head is None:
            print("empty")
            return
        cur = self.head
        while cur:
            print(cur.data,end="->")
            cur = cur.next

    def e_insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return
        cur = self.head
        while cur.next:
          cur = cur.next
        cur.next = newnode

    def b_delete(self):
        if self.head is None:
            print("empty")
            return
        self.head  = self.head.next

    def e_delete(self):
        if self.head is None:
            print("empty")
            return
        if self.head.next is None:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next =None

    def find_position(self,pos):
        cur = self.head
        for i in range(pos-1):
            if cur.next is None:
                # print("no position found")
                # break
                return -1
            cur = cur.next
        # else: print(cur.data)
        return cur

    def insert_by_position(self,data,pos):
        newnode = Node(data)
        if pos == 1:
            self.b_insert(data)
            return
        cur = self.find_position(pos-1)
        if cur == -1:
            print("no position found")
        else:
            newnode.next = cur.next
            cur.next=newnode

obj = linkedlist()
obj.e_insert(20)
obj.b_insert(90)
obj.b_insert(70)
obj.display()
print()
# obj.e_delete()
# obj.display()
obj.find_position(8)
obj.insert_by_position(1,2)
obj.display()