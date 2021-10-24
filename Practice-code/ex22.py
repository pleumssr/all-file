class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty()==True:
            return ''
        else :
            cur= self.head
            s=''
            for i in range(self.size()-1):
                s += str(cur.value) + "->"
                cur = cur.next
            s += str(cur.value)
            return s
    def str_reverse(self):
        if self.isEmpty()==True:
            return ""
        else :
            cur= self.head
            while cur.next != None:
                cur=cur.next
            s=''
            for i in range(self.size()-1):
                s += str(cur.value) + "->"
                cur = cur.prev
            s += str(cur.value)
            return s

    def isEmpty(self):
        return self.head == None

    def append(self, new_data):
 
        new_node = Node(new_data)
        last = self.head
 
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
 
        else :
            while (last.next is not None):
                last = last.next
            last.next = new_node
            new_node.prev = last

    def addHead(self, new_data):
        new_node = Node(new_data)
    
        new_node.next = self.head
        new_node.prev = None
    
        if self.head is not None:
            self.head.prev = new_node
    
        self.head = new_node

    def insertBefore(self, index, new_data):
        if index <0:
            print("Data cannot be added")
            return
        if index == 0:
            self.addHead(new_data)
            print('index = '+str(index)+" and data = "+str(new_data))
        elif index == self.size():
            self.append(new_data)
            print('index = '+str(index)+" and data = "+str(new_data))
        else:
            node=self.head
            for i in range(index):
                node=node.next
            prenode=self.head
            for i in range(index-1):
                prenode=prenode.next
            
            

            new_node = Node(new_data)
            
    
            new_node.prev = node.prev
    
            node.prev = new_node
    
            new_node.next = node

            prenode.next=new_node

            print('index = '+str(index)+" and data = "+str(new_data))

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
            try:
                for i in range(self.size()):
                    if temp.value==item:
                        index=i
                        return index   
                    else:
                        temp=temp.next
            except:pass
            return -1

    def size(self):
        if self.isEmpty():
            return 0
        else:
            temp=self.head
            nub=1
            while temp.next!=None:
                temp=temp.next
                nub+=1
            return nub
    def remove(self,data):
        rin=data
        cur=self.head
        
        if self.index(int(data))==-1:
            print('Not Found!')
            return
        index=int(self.index(int(data)))
        if index == 0 and self.size()==1:
            self.head=cur.next
            print('removed : '+str(rin)+" from index : "+str(index))
        elif index == 0:
            self.head=cur.next
            self.head.prev=None
            print('removed : '+str(rin)+" from index : "+str(index))
        elif index == self.size()-1:
            last=self.head
            for i in range(self.size()-1):
                last=last.next
            last.prev = None
            for i in range(self.size()-2):
                cur=cur.next
            cur.next=None
            print('removed : '+str(rin)+" from index : "+str(index))
        else:
            node=self.head
            for i in range(index):
                node=node.next
            prenode=self.head
            for i in range(index-1):
                prenode=prenode.next
            nextnode=self.head
            for i in range(index+1):
                nextnode=nextnode.next
            
            if node is None:
                print("Data cannot be added")
                return

            prenode.next=node.next
            nextnode.prev=node.prev

            print('removed : '+str(rin)+" from index : "+str(index))


L = LinkedList()
inp = [x.split() for x in input('Enter Input : ').split(',')]
for i in inp:
    if i[0] == "A":
        L.append(int(i[1]))
        print("linked list :", L)
        print("reverse :",L.str_reverse())
    elif i[0] == "Ab":
        L.addHead(int(i[1]))
        print("linked list :", L)
        print("reverse :",L.str_reverse())
    elif i[0] == "I":
        index,data=i[1].split(':')
        try:
            L.insertBefore(int(index),int(data))
        except:
            print('Data cannot be added')
        print("linked list :", L)
        print("reverse :",L.str_reverse())
    elif i[0] == "R":
        L.remove(int(i[1]))
        print("linked list :", L)
        print("reverse :",L.str_reverse())

