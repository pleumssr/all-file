class Stack():
    def __init__(self,list=None):
        if list == None:
            self.item = []
        else:
            self.item = list
    
    def __str__(self):
        for i in self.item:
            print(i,end=" ")

    def push(self,i):
        self.item.append(i)

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

S = Stack()


inp = [x.split() for x in input('Enter Input : ').split(',')]
# print(inp)
for i in inp:
    if i[0]=='A':
        S.push(i[1])
    elif i[0]=='B':
        maxtree=0
        seetree=0
        for j in range(len(S.item)-1,-1,-1):
            # print(S.item[j])
            if int(S.item[j]) > maxtree:
                seetree+=1
                maxtree=int(S.item[j])
        print(seetree)
            
### Enter Your Code Here ###