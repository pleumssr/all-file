class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty()==True:
            return ''
        else :
            cur= self.head
            s=''
            while cur.next !=None:
                s += str(cur.data) + " "
                cur = cur.next
            s += str(cur.data)
            return s
    
    def isEmpty(self):
        return self.head==None

    def add(self,data):
        if self.isEmpty()==True:
            self.head=Node(data)
            self.head.next=Node('|')
        else:
            cur=self.head
            new_node = Node(data)
            while cur.next.data!='|':
                cur=cur.next
            # add node (next and prev)
            befor_node=cur
            after_node=cur.next
            befor_node.next=new_node
            new_node.prev=befor_node
            new_node.next=after_node
            after_node.prev=new_node

    def indexl(self):
        cur=self.head
        index=0
        while cur.data!='|':
            index+=1
            cur=cur.next
        return index
    
    def left(self):
        if self.isEmpty():
            return
        cur = self.head
        #หา node2
        if self.indexl()==0:
            cur=self.head
        else:
            while cur.next.data!='|':
                cur=cur.next
        if self.indexl()==0:
            pass
            return
        if self.indexl()==1:
            if self.size()==2:
                node1=cur
                node2=cur.next
                self.head=node2
                node2.prev=None
                node2.next=node1
                node1.prev=node2
                node1.next=None
            else :
                node1=cur
                node2=cur.next
                node3=cur.next.next
                self.head=node2
                node2.prev=None
                node2.next=node1
                node1.prev=node2
                node1.next=node3
                node3.prev=node1
            return
        if self.indexl()==self.size()-2:
            node0=cur.prev
            node1=cur
            node2=cur.next#('|')
            node3=cur.next.next
            node0.next=node2
            node2.prev=node0
            node2.next=node1
            node1.prev=node2
            node1.next=node3
            node3.prev=node1
            return
        if self.indexl()==self.size()-1:
            node1=cur.prev
            node2=cur
            node3=cur.next#('|')
            node1.next=node3
            node3.prev=node1
            node3.next=node2
            node2.prev=node3
            node2.next=None
            return
        #สลับ node3('|')-node2 
        node1=cur.prev
        node2=cur
        node3=cur.next
        node4=cur.next.next
        node1.next=node3
        node3.prev=node1
        node3.next=node2
        node2.prev=node3
        node2.next=node4

    def Right(self):
        if self.isEmpty():
            return
        cur = self.head
        #หา node 2('|')
        while cur.data!='|':
            cur=cur.next
        if self.indexl()==0:
            if self.size()==2:
                node1=cur
                node2=cur.next
                self.head=node2
                node2.next=node1
                node1.prev=node2
                node1.next=None
                node2.prev=None
            else :
                node1=cur
                node2=cur.next
                node3=cur.next.next
                node2.prev=None
                node2.next=node1
                node1.prev=node2
                node1.next=node3
                node3.prev=node1
                self.head=node2
            return
        if self.indexl()==self.size()-2:
            node1=cur.prev
            node2=cur
            node3=cur.next

            node1.next=node3
            node3.prev=node1
            node3.next=node2
            node2.prev=node3
            node2.next=None
            return
        if self.indexl()==self.size()-1:
            pass
            return
        #สลับ node3-node2('|') 
        node1=cur.prev
        node2=cur
        node3=cur.next
        node4=cur.next.next

        node1.next=node3
        node3.prev=node1
        node3.next=node2
        node2.prev=node3
        node2.next=node4
        node4.prev=node2
    def delR(self):
        cur=self.head
        while cur.data!='|':
            cur=cur.next
        if self.indexl()==self.size()-1:
            pass
            return
        if self.size()==2:
            cur.next=None
            return
        if self.indexl()==self.size()-2:
            node1=cur
            node2=cur.next
            node1.next=None
            node2.prev=None
            return
        node1=cur
        node3=cur.next.next
        node1.next=node3
        node3.prev=node1

    def delL(self):
        cur=self.head
        while cur.data!='|':
            cur=cur.next
        if self.indexl()==0:
            pass
            return
        if self.size()==2:
            self.head=cur
            cur.prev=None
            return
        if self.indexl()==1:
            self.head=cur
            cur.prev=None
        node1=cur.prev.prev
        node3=cur
        node1.next=node3
        node3.prev=node1


    def size(self):
        cur=self.head
        nub=0
        while cur!=None:
            nub+=1
            cur=cur.next
        return nub
        
        
inp= [x.split() for x in input("Enter Input : ").split(',')]
L=LinkedList()
for i in inp:
    if i[0] == "I":
            L.add(str(i[1]))
    elif i[0] == "L":
            L.left()
    elif i[0] == "R":
            L.Right()
    elif i[0] == "D":
            L.delR()
    elif i[0] == "B":
            L.delL()

print(L)