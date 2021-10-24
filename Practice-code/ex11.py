class stack():

    def __init__(self,item):
        for i in item:
            self.item.append(i)

    def __str__(self) -> str:
        for i in self.item:
            print(i)

    def size(self):
        return len(self.item)

    def push(self,item):
        self.item.append(item)
    
    def pop(self):
        self.item.pop()

    def isEmty(self):
        return self.item==[]

    def peek(self,i=-1):
        if self.isEmty()==False:
            return self.item[i]

li = input("Enter Input : ").split(",")
#print(li)
stk = stack()
for i in li:

    if i[0]=='A':
        
        s=''
        for j in range(1,len(i)):
            s+=i[j]
        stk.push(int(s))
        print("Add ="+s+" and Size = "+str(stk.size()))

    elif i[0]=='P':
        if stk.isEmty()==False:
            print("Pop = "+str(stk.peek())+" and Index = "+str(stk.size()-1))
            stk.pop()
        else :
            print("-1")


if stk.isEmty()==False:
    print("Value in Stack =",end="")

    for i in range(stk.size()):
        print(" "+str(stk.peek(i)),end="")
    print("")
elif stk.isEmty()==True:
    print("Value in Stack = Empty")



    