class stack():
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

    def pop(self):
        if self.isEmpty()==False:
            return self.item.pop()
        else :
            return False

    def peek(self):
        if self.isEmpty()==False:
            return self.item[-1]
        else :
            return False

    def isEmpty(self):
        if self.item==[]:
            return True
        else :
            return False 

    def size(self):
        return len(self.item)
data = input("Enter expresion : ") #{{{][]}}}
print(data,end=' ')
data=list(data)
isCheck=False
st = stack()
for i in data:
    if i in '([{':
        st.push(i)
    elif i in ')]}':
        if i==')':
            if st.peek()=='(': st.pop()
            elif st.peek()==False:
                print("close paren excess")
                isCheck=True
                break
            else : 
                print("Unmatch open-close")
                isCheck=True
                break
        elif i=='}':
            if st.peek()=='{': st.pop()
            elif st.peek()==False :
                 print("close paren excess")
                 isCheck=True
                 break
            else :
                print("Unmatch open-close  ")
                isCheck=True
                break
        elif i==']':
            if st.peek()=='[': st.pop()
            elif st.peek()==False :
                 print("close paren excess")
                 isCheck=True
                 break
            else :
                 print("Unmatch open-close  ")
                 isCheck=True
                 break
if st.size()!=0 and isCheck==False:
    print("open paren excess   "+str(st.size())+" : ",end='')
    for i in st.item:
        print(i,end='')
elif st.size()==0 and isCheck==False:
    print("MATCH")