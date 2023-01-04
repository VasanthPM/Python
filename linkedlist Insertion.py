class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __int__(self):
        self.head = None

    def insert_beg(self, data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_last(self,data):
        nl = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = nl

    def insert_postion(self,data,pos):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.next = temp.next
        temp.next = np

    def Display(self):
        temp = self.head
        if temp is None:
            print("List is Empty")
        else:
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next


l = Linkedlist()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
#l.Display()
l.insert_beg(5)
l.insert_last(12)
l.insert_postion(34,3)
l.Display()
