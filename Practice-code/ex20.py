
class queue():
    def __init__(self,item=None):
        if item==None:
            self.item=[]
        else : self.item=list(item)    
        self.boomlis=[]
        self.countBoom=0
        self.countFail=0

    def __str__(self):
        s=''
        for i in self.item:
            s+=i
        return s        
    
    def push(self,i):
        self.item.append(i)

    def pop(self,i=0):
        self.item.pop(i)
    
    def peek(self,i=-1):
        return self.item(i)
    
    def size(self):
        return len(self.item)

    def isEmpty(self):
        if self.item == []:
            return True
        else : return False
    
    def checkBoom(self):
        lenn=len(self.item)
        i=2
        while i<len(self.item):
                try:
                    if self.item[i] == self.item[i-1] and self.item[i]== self.item[i-2]:
                        self.boomlis.append(self.item[i])
                        self.item.pop(i)
                        self.item.pop(i-1)
                        self.item.pop(i-2)
                        self.countBoom+=1
                        i=2
                    else :i+=1
                except:
                    i+=1
                    continue
    
    def addBoom(self):
        lenn=len(self.item)
        i=2
        while i<lenn:
                try:
                    if self.item[i] == self.item[i-1] and self.item[i]== self.item[i-2]:
                        self.item.insert(i,self.boomlis.pop(0))
                        lenn+=1
                        if self.item[i] == self.item[i-1] and self.item[i]== self.item[i-2]:
                            # self.boomlis.append(self.item[i])
                            self.item.pop(i)
                            self.item.pop(i-1)
                            self.item.pop(i-2)
                            self.countFail+=1
                    else : i+=1
                except:
                    i+=1
                    continue
def rev(string1):
    s=''
    for i in range(len(string1)-1,-1,-1):
        s+=string1[i]
    return s


inp = [i for i in input("Enter Input (Normal, Mirror) : ").split()]
normlis = queue(inp[0])
mirrlis = queue(rev(inp[1]))
mirrlis.checkBoom()
normlis.boomlis=mirrlis.boomlis
normlis.addBoom()
normlis.checkBoom()
print("NORMAL :")
print(normlis.size())
if normlis.size()!=0:
    print(rev(normlis.item))
else : print("Empty")
print(str(normlis.countBoom)+" Explosive(s) ! ! ! (NORMAL)")
if normlis.countFail>0:
    print("Failed Interrupted "+str(normlis.countFail)+ " Bomb(s)")
print("------------MIRROR------------")
print(rev("MIRROR :"))
print(mirrlis.size())
if mirrlis.size()!=0:
    print(rev(mirrlis.item))
else : print(rev("Empty"))
print("(RORRIM) ! ! ! (s)evisolpxE "+str(mirrlis.countBoom))