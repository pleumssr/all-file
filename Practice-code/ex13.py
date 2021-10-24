class Stack():
    def __init__(self,list=None):
        if list == None:
            self.item = []
        else:
            self.item = list
    
    def __str__(self):
        s=''
        for i in self.item:
            s+=str(i)
        return s

    def push(self,i):
        self.item.append(i)

    def pop(self,i=-1):
        if self.isEmpty() == False:
            return self.item.pop(i)


    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        if self.item==[]:
            return True
        else :
            return False 

    def size(self):
        return len(self.item)

def postFixeval(st):

    s = Stack()
    for i in st :
        if len(i)==1:
            if i in '+-*/':
                if i=='+':
                    total=s.pop(-2)+s.pop(-1)
                elif i=='-':
                    total=s.pop(-2)-s.pop(-1)
                elif i=='*':
                    total=s.pop(-2)*s.pop(-1)
                elif i=='/':
                    total=s.pop(-2)/s.pop(-1)
                s.push(total)

            else : s.push(float(i))

        else : s.push(float(i))
    return s.pop()

print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

#print(token)

#print(f"Answer : {postFixeval(token):.2}")
print("Answer : ",'{:.2f}'.format(postFixeval(token)))