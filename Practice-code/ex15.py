class Stack :
    def __init__(self,list=None):
        if list == None:
            self.item = []
        else:
            self.item = list
    
    def __str__(self):
        for i in self.item:
            print(i,end=" ")
        #print(s)

    def push(self,i):
        self.item.append(i)
        #s.push()

    def pop(self,i=-1):
        if self.isEmpty()==False:
            return self.item.pop(i)

    def peek(self,i=-1):
        if self.isEmpty()==False:
            return self.item[i]

    def isEmpty(self):
        if self.item==[]:
            return True
        else :
            return False 

    def size(self):
        return len(self.item)
    

def dec2bin(decnum):
    s = Stack()
    st=''
    maxbit=0
    while 2**maxbit<=decnum:
        maxbit+=1
    for i in range(maxbit-1,-1,-1):
        if 2**i<=decnum:
            s.push(1)
            decnum-=2**i
        else : s.push(0)
    for i in s.item:
        st+=str(i)
    return st


    

    ### Enter Your Code Here ###

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))