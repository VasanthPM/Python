class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __int__(self):
        self.head = None

    def delete_beg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None

    def delete_end(self):
        temp = self.head.next
        prev=self.head
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next=None

    def delete_pos(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next


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
n3 = Node(13)
n2.next = n3
n4 = Node(45)
n3.next = n4
n5 = Node(95)
n4.next = n5
#l.delete_beg()
#l.delete_end()
l.delete_pos(3)
l.Display()
