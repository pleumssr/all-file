class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        try:
            cur, s = self.head, str(self.head.value) + " "
            while cur.next != None:
                s += str(cur.next.value) + " "
                cur = cur.next
            return s
        except:return "Empty"

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty():
            self.head=Node(item)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(item)

    def addHead(self, item):
        if self.isEmpty():
            self.head=Node(item)
        else:
            q=self.head
            self.head=Node(item)
            self.head.next=q

    def search(self, item):
        check='Not Found'
        try:
            temp = self.head
            for i in range(self.size()):
                if temp.value==item:
                    check='Found'
                    break    
                else:
                    temp=temp.next
            return check
        except:return check

    def index(self, item):
            temp = self.head
            index=-1
            try:
                for i in range(self.size()):
                    if temp.value==str(item):
                        index=i
                        break    
                    else:
                        temp=temp.next
            except:pass
            return index

    def size(self):
        if self.isEmpty():
            return 0
        try:
            temp=self.head
            nub=1
            while temp.next!=None:
                temp=temp.next
                nub+=1
            return nub
        except:return nub

    def pop(self, pos):
        try:
            temp = self.head
            if int(pos)==0:
                for i in range(int(pos)+1):
                    temp=temp.next
                self.head=temp
                return "Success"
            else:
                for i in range(int(pos)):
                    temp=temp.next
                q=temp.next
                temp = self.head
                for i in range(int(pos)-1):
                    temp=temp.next
                temp.next=q
                return "Success"
        except:return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)