class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

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
        except:return ""
    
    def str_reverse(self):
        if self.isEmpty()==True:
            return ""
        else :
            cur= self.head
            while cur.next != None:
                cur=cur.next
            s=''
            for i in range(self.size()-1):
                s += str(cur.value) + " "
                cur = cur.prev
            s += str(cur.value)
            return s

    def str_reverse_to(self):
        if self.isEmpty()==True:
            return ""
        else :
            cur= self.head
            while cur.next != None:
                cur=cur.next
            s=''
            for i in range(self.size()-1):
                s += str(cur.value) + "-> "
                cur = cur.prev
            s += str(cur.value)
            return s

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

    def pop(self, pos):
        cur = self.head
        if self.isEmpty():
            return
        if cur.next==None:
            num=self.head
            self.head=None
            return num.value
        if pos==0:
            num=self.head
            self.head=cur.next
            return num.value
        for i in range(pos-1):
            cur=cur.next
        num=cur.next
        cur.next=cur.next.next
        return num.value
    
    def sort_all(self):
        if self.isEmpty():
            return
        cur=self.head
        data=[]
        while cur!=None:
            data.append(cur.value)
            cur=cur.next
        data.sort()
        cur=self.head
        i=0
        while cur!=None:
            cur.value=data[i]
            cur=cur.next
            i+=1
        




def get_digit(n,d):
    for i in range(d-1):
        n//=10
    return n%10
def get_max_bits(n):
    i=0
    while n>0:
        n//=10
        i+=1
    return i
def radix_sort(l):
    before_list=list(l)
    li=l
    L=[]
    for i in range(10):
        L.append(LinkedList())

    max_bits= get_max_bits(max(li))#หาหลักที่มากสุด
    for i in range(1,max_bits+2):
        while len(li)!=0:
            # print(li)
            num = li.pop(0)
            num_digit = get_digit(num,i)
            L[num_digit].append(num)
            # get num to Linke list each num
        print("------------------------------------------------------------")
        print("Round :",i)
        for i in range(10):
            L[i].sort_all()
            print(i,":",L[i].str_reverse())
        for i in range(10):
            while not L[i].isEmpty():
                li.append(L[i].pop(0))
    print("------------------------------------------------------------")
    print(max_bits,"Time(s)")
    print("Before Radix Sort : ",end='')
    for i in range(len(before_list)-1):
        print(before_list[i],"-> ",end='')
    print(before_list[-1])
    print("After  Radix Sort : ",end='')
    for i in range(len(before_list)-1,0,-1):
        print(li[i],'-> ',end='')
    print(li[0])
    


L = LinkedList()
inp = list(map(int,input('Enter Input : ').split()))
# print(inp)
radix_sort(inp)
