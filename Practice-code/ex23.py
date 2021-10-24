class node:
    def __init__(self,data,next = None ):
        self.data=data
        self.next=next
    # def __str__(self):
        

def createList(l=[]):
    node_list=[]
    for i in range(len(l)):
        node_list.append(node(l[i]))
    head=node_list[0]
    for i in range(len(l)):
        if i == len(l)-1:
            node_list[i].next=None
        else :
            node_list[i].next=node_list[i+1]
    return head

def printList(H):
    s=''
    cur=H
    while cur != None:
        s+=str(cur.data)+" "
        cur=cur.next
    print(s)
def mergeOrderesList(p,q):
    ll1=p
    ll2=q
    cur=ll1
    # conect ll1 and ll2
    while cur.next != None:
        cur=cur.next 
    cur.next=ll2
    #sort data
    mergelist=[]
    mergell=ll1
    while mergell != None:
        mergelist.append(mergell.data)
        mergell=mergell.next
    for i in range(len(mergelist)):
        for j in range(i,len(mergelist)):
            if int(mergelist[j])<=int(mergelist[i]):
                temp=mergelist[i]
                mergelist[i]=mergelist[j]
                mergelist[j]=temp
    m =createList(mergelist)
    return m

L = [i.split(',') for i in input("Enter 2 Lists : ").split()]

LL1 = createList(L[0])
LL2 = createList(L[1])
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)