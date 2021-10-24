inp = [i for i in input("Enter people : ")]
# print(inp)
q1= []
q2= []
count=0
scope = len(inp)
for i in range(scope):
    count+=1
    print(count,end=" ")
    if count%2==0:
         if len(q2)>0:
            q2.pop(0)
    
    if len(q1)<5:
        q1.append(inp[0])
        inp.pop(0)
    elif len(q2)<5:
        q2.append(inp[0])
        inp.pop(0)
    print(inp,end=' ')
    print(q1,end=' ')
    print(q2)
    if count%3==0:
         if len(q1)>0:
            q1.pop(0)
    
