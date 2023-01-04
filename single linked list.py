class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __int__(self):
        self.head = None

    def Display(self):
        temp = self.head
        if temp is None:
            print("List is Empty")
        else:
            while temp:
                print(temp.data,"-->",end=" ")
                temp = temp.next

l = Linkedlist()
n1 = Node(10)
l.head = n1
n2 = Node(20)
n1.next = n2
l.Display()
