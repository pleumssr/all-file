x = [x.split() for x in input("Enter Input : ").split(',')]
q = []
outofindex = False
# print(x)
for i in x:
    if i[0]=='E':
        print("Add "+str(i[1])+" index is "+str(len(q)))
        q.append(i[1])
    elif i[0]=='D':
        if len(q)==0:
            print("-1")
            outofindex = True
        else:
            print("Pop "+str(q.pop(0))+" size in queue is "+str(len(q)))
if len(q)>0:
    print("Number in Queue is :  ",end='')
    print(q)
else :
    print("Empty")
